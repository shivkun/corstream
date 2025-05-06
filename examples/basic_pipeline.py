# examples/basic_pipeline.py
# version 0.1.0

import asyncio
from corstream import Stream

# Simulated async function to get "emails"
async def get_email(user_id: int) -> str:
    await asyncio.sleep(0.01)
    return f"user{user_id}@example.com"

# Simulated async sink to "send" emails
async def send_email_batch(batch: list[str]) -> None:
    print(f"Send emails to: {batch}")
    await asyncio.sleep(0.05)
    
async def main():
    await (
        Stream
        .from_iterable(range(1, 11))            # User IDs from 1 to 10
        .filter(lambda uid: uid % 2 == 0)        # Even-numbered users only
        .map(get_email)                         # Fetch email addresses
        .batch(3)                               # Group emails into batches of 3
        .for_each(send_email_batch)             # Send each batch
    )
    
if __name__ == "__main__":
    asyncio.run(main())