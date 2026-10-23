class Solution:

    def encode(self, strs: List[str]) -> str:
        e_strs = ''
        for str in strs:
            e_strs += (".+" + str)

        return e_strs

    def decode(self, s: str) -> List[str]:
        s = s.split(".+")[1:]
        return s


