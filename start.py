import hashlib as hl

print(hl.sha256(input().encode()).hexdigest())
