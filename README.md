# 2491. Divide Players Into Teams of Equal Skill

__Type:__ Medium<br>
__Topics:__ Array, Hash Table, Two Pointers, Sorting<br>
__Companies:__ Amazon, Expedia, IBM, Uber<br>
<hr>

You are given a positive integer array `skill` of even length `n` where `skill[i]` denotes the skill of the <code>i<sup>th</sup></code> player. Divide the players into `n / 2` teams of size `2` such that the total skill of each team is equal.

The __chemistry__ of a team is equal to the __product__ of the skills of the players on that team.

Return _the sum of the __chemistry__ of all the teams, or return_ `-1` _if there is no way to divide the players into teams such that the total skill of each team is equal._
<hr>

__Example 1:__<br>

__Input:__ skill = [3,2,5,1,3,4]<br>
__Output:__ 22<br>
__Explanation:__<br>
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.<br>
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

__Example 2:__ <br>

__Input:__ skill = [3,4]<br>
__Output:__ 12<br>
__Explanation:__<br>
The two players form a team with a total skill of 7.<br>
The chemistry of the team is 3 * 4 = 12.

__Example 3:__ <br>

__Input:__ skill = [1,1,2,3] <br>
__Output:__ -1 <br>
__Explanation:__ <br>
There is no way to divide the players into teams such that the total skill of each team is equal.
<hr>

### Constraints:

- <code>2 <= skill.length <= 10<sup>5</sup></code>
- `skill.length` is even.
- `1 <= skill[i] <= 1000`
<hr>

### Hints:
- Try sorting the skill array.
- It is always optimal to pair the weakest available player with the strongest available player.