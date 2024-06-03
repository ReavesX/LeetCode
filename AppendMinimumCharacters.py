class Solution:
  # Runtime 62ms
  # memory usage: 17.46 mb 
  # difficulty: medium
    def appendCharacters(self, s: str, t: str) -> int:

      
      """
        Returns the minimum number of characters needed to be appended to string `s`
        so that string `t` becomes a subsequence of `s`.

        Args:
        - s (str): The input string `s` to which characters may be appended.
        - t (str): The target string `t` that should become a subsequence of `s`.

        Returns:
        - int: The minimum number of characters needed to be appended to `s` to make `t` a subsequence.

        Raises:
        - ValueError: If either `s` or `t` is `None`.
        """
      
        if s is None or t is None:
            raise ValueError('There is no value')
        i,j = 0,0

        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1  

        return len(t) - j 
