class Solution:
    def singleNumber(self, a: List[int]) -> List[int]:
        all_xor = 0
        for e in a:
            all_xor ^= e
        
        shift = 0
        while (all_xor>>shift) != 0 and ((all_xor>>shift) & 1) != 1:
            shift += 1

        grp1, grp2 = 0, 0

        for e in a:
            if (e>>shift) & 1 == 1:
                grp1 ^= e
            else:
                grp2 ^= e
        
        return [grp1, grp2]