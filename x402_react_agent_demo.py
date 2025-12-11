""" ReAct agent demo for x402 payments."""
import asyncio
import os
import json
from decimal import Decimal
from typing import Any

from eth_account import Account

from spoon_ai.agents.spoon_react import SpoonReactAI
from spoon_ai.chat import ChatBot
from spoon_ai.payments import X402PaymentReceipt, X402PaymentService
from spoon_ai.tools.tool_manager import ToolManager
from spoon_ai.tools.x402_payment import X402PaywalledRequestTool
from spoon_toolkits.web.web_scraper import WebScraperTool
from x402.encoding import safe_base64_decode
from dotenv import load_dotenv

load_dotenv(override=True)
PAYWALLED_URL = os.getenv("X402_DEMO_URL", "https://www.x402.org/protected")
PAYMENT_USDC = Decimal("0.01")

def setup_wallet(service: X402PaymentService) -> None:
    """Configures wallet and address, failing fast if missing."""
    client = service.settings.client
    if not client.private_key and not client.use_turnkey:
        raise ValueError("Missing configuration: Set PRIVATE_KEY or enable Turnkey.")

    if client.private_key and not client.private_key.startswith("0x"):
        client.private_key = "0x" + client.private_key

    # Infer address if not set
    if not service.settings.pay_to or service.settings.pay_to.startswith("0xYourAgent"):
        if client.private_key:
            service.settings.pay_to = Account.from_key(client.private_key).address
        elif client.turnkey_address:
            service.settings.pay_to = client.turnkey_address
        else:
            raise ValueError("Cannot determine wallet address.")
    
    # Cap payment amount safety
    service.settings.max_amount_usdc = min(service.settings.max_amount_usdc or PAYMENT_USDC, PAYMENT_USDC)

class X402ReactAgent(SpoonReactAI):
    name: str = "x402_agent"
    
    def __init__(self, service: X402PaymentService, url: str, **kwargs: Any) -> None:
        super().__init__(service=service, target_url=url, **kwargs)
        self.payment_tool = X402PaywalledRequestTool(service=service)
        self.web_scraper = WebScraperTool()
        self.available_tools = ToolManager([self.web_scraper, self.payment_tool])
        
        # Compact prompt: Trust the agent to handle logic
        tool_desc = self._build_tool_list()
        self.system_prompt = (
            f"TARGET: {url}\n"
            "You are an agent executing an x402 payment demonstration. Follow this strict sequence:\n"
            "1. FIRST, call `web_scraper` on the target. Verify it fails with '402 Payment Required'.\n" 
            f"2. THEN, use `x402_paywalled_request` (amount={PAYMENT_USDC}) to pay and access the content.\n" 
            "3. FINALLY, verify the content is unlocked and summarise the music track details.\n"
            f"\nTools:\n{tool_desc}"
        )

async def main():
    print("x402 ReAct Agent Demo")
    
    # Initialize
    service = X402PaymentService()
    setup_wallet(service)
    
    agent = X402ReactAgent(service=service, url=PAYWALLED_URL, llm=ChatBot())
    
    print(f"Payer: {service.settings.pay_to} | Target: {PAYWALLED_URL}")
    print("Running agent...")

    await agent.run(f"Access {PAYWALLED_URL}, pay if needed, and summarise the content.")
    
    # Output Results
    messages = agent.memory.get_messages()
    last_assistant_msg = next((m for m in reversed(messages) if m.role == "assistant"), None)
    
    if last_assistant_msg:
        print("\nAgent Result:")
        print(last_assistant_msg.content)

    # Attempt to find and print the technical receipt from the logs for verification
    for msg in reversed(messages):
        if msg.role == "tool" and msg.name == "x402_paywalled_request" and msg.content:
            try:
                data = json.loads(msg.content) if isinstance(msg.content, str) else msg.content
                if isinstance(data, dict):
                    # Check for direct receipt or header
                    receipt_header = (data.get("headers") or {}).get("X-PAYMENT-RESPONSE")
                    if receipt_header:
                        receipt = X402PaymentReceipt.model_validate_json(safe_base64_decode(receipt_header))
                        print("\nPayment Confirmed (Receipt Decoded):")
                        print(json.dumps(receipt.model_dump(), indent=2))
                        break
            except Exception:
                continue

if __name__ == "__main__":
    asyncio.run(main())