from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the skill levels to facilitate pairing
        skill.sort()
        
        # Initialize total skill product, left pointer, and right pointer
        total_skill_product = 0  # This will accumulate the total product of skill pairs
        left_pointer = 0         # Pointer starting from the beginning of the sorted skill list
        right_pointer = len(skill) - 1  # Pointer starting from the end of the sorted skill list
        
        # Calculate the target sum for pairing
        target_sum = skill[left_pointer] + skill[right_pointer]

        # Iterate while the left pointer is less than the right pointer
        while left_pointer < right_pointer:
            # Check if the sum of the current pair equals the target sum
            if skill[left_pointer] + skill[right_pointer] == target_sum:
                # If it matches, add the product of the current pair to the total
                total_skill_product += (skill[left_pointer] * skill[right_pointer])
            else:
                # If the sum does not match the target, return -1 as it's not possible to pair
                return -1

            # Move the pointers inward to check the next pair
            left_pointer += 1
            right_pointer -= 1

        # Return the total product of skills for valid pairs
        return total_skill_product