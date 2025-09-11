# ez Corrupted Memory Dump

"Our server was hacked, and the attacker left behind a corrupted memory dump. We managed to extract this suspicious file, but it’s not what it seems. The flag is hidden deep within the dump, but beware of decoys and misleading data!"

## Objective
Your task is to recover the real flag hidden in the memory dump. Be careful—there are fake flags and misleading data scattered throughout the file to throw you off track.

## File Provided
- `corrupted_dump.bin`: The corrupted memory dump file.

## Hints (If Stuck)
1. "Not all memory is what it seems. Look beyond the headers."
2. "Common XOR keys are 0xAA, 0x55, or 0xFF."
3. "The flag is 30 bytes long, starting at offset 0x10000."
4. "Fake flags are XOR-encoded with a different key than the real flag."
5. "Analyze the structure of the flag to identify the real one."

## Rules
- The flag format is `MED{...}`.
- Only one flag is the real one. Fake flags are there to mislead you.
- Use your skills in memory forensics and XOR decoding to recover the correct flag.

## Tools You Might Need
- A hex editor to inspect the memory dump.
- Python or any scripting language to automate XOR decoding.
- Patience and attention to detail to distinguish the real flag from the fake ones.

Good luck, and happy hunting!
