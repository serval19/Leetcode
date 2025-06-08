
class Solution:
    def reverseBits(self, n):
        binary=bin(n)
        binary=binary[2:]
        extrazeroes=32-len(binary)
        binary="0" * extrazeroes + binary
        revbinary=binary[::-1]
        num=int(revbinary,2)
        return num
