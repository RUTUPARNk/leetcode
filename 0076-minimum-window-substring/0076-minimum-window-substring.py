class Solution:
    """
    Finds the minimum substring of S that contains all characters of T.
    Uses the Sliding Window technique with two hash maps.
    """
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If t is empty, the result is an empty string.
        if not t:
            return ""

        # 1. Initialize character frequency map for T (t_map)
        # This stores the required count for each character in t.
        t_map = collections.Counter(t)

        # 2. Variables for the sliding window
        window_map = collections.defaultdict(int)  # Frequencies of chars in the current window
        
        # 'required_count' is the number of unique characters in t (e.g., 3 for "AABC")
        required_count = len(t_map)
        
        # 'have_count' is the number of unique characters the current window has matched 
        # the frequency requirement for (e.g., 2 if 'A' is matched and 'B' is matched, 
        # but 'C' is not yet matched).
        have_count = 0
        
        left = 0
        
        # Variables to store the minimum window result
        min_len = float('inf')
        min_start_index = -1

        # 3. Expand the window (Move the right pointer)
        for right in range(len(s)):
            char_r = s[right]
            
            # Add the new character to the window_map
            window_map[char_r] += 1

            # Check if this character helps fulfill the requirement for a unique char
            if char_r in t_map and window_map[char_r] == t_map[char_r]:
                have_count += 1

            # 4. Shrink the window (Move the left pointer) if the window is valid
            while have_count == required_count:
                # The window is valid: check if this is the minimum length found so far
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_start_index = left

                # Get the character to be removed from the left side
                char_l = s[left]
                
                # Update window_map by removing the character at 'left'
                window_map[char_l] -= 1

                # Check if removing this character makes the window invalid
                if char_l in t_map and window_map[char_l] < t_map[char_l]:
                    # If the count drops below the requirement, we lose a unique match
                    have_count -= 1

                # Move the left pointer to shrink the window
                left += 1

        # 5. Return the minimum window substring
        if min_start_index == -1:
            return ""
        
        return s[min_start_index : min_start_index + min_len]
