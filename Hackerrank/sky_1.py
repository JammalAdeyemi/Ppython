# You are given a string representing a sequence of N arrows, each pointing in one of the four cardinal 
# directions: up (**), down (v), left (<) or right (>). Write a function solution that, given a string S 
# denoting the directions of the arrows, returns the minimum number of arrows that must be rotated to 
# make them all point in the same direction. Examples:
# Given S = "W<v", the function should retu 2. After rotating both the first () and fourth (<) arrows 
# downwards (V), all of the arrows would point down.
# Given S = "vs>>w", the function should return 3. After rotating the first, fifth and sixth arrow 
# rightwards, all of the arrows would point right.
# Given S = "«<<" the function should return O. All of the arrows already point left. Assume that: 
# • N is an integer within the range [1..100); • string S is made only of the following characters: ^ v,< and/or>.
def solution(S):
    # Implement your solution here
    counts = [0, 0, 0, 0]
    for i in range(len(S)):
        direction = S[i]
        if direction == '^':
            counts[0] += 1
        elif direction == 'v':
            counts[1] += 1
        elif direction == '<':
            counts[2] += 1
        else:
            counts[3] += 1
    max_count = 0
    for i in counts:
        max_count = max(max_count, i)
    rotations = len(S) - max_count

    return rotations
    
# Given a txt file that emulates an environment file a text file containing an app's configuration), 
# implement the function parse_config (config_file) where config_file is a string. The function takes a 
# path to a config file as an argument, transforms its content into a dictionary and returns that 
# dictionary. For example, this is how the environment file would look: 
# secret_token=0.523jf489630rew And when converted into a dictionary it should look like this: 
#   {' secret_token': '0.523jf489630rew'} 
# In other words, whatever comes after the first '=' is the value, which will always be a string, 
# meaning that nested values are not expected. Each non((-))empty line represents a new element in the 
# dictionary. 
# Hints 
# • Make sure to ignore the blank lines. 
# • Make sure to ignore the comments, which are the lines starting with # 
# • Keep in mind that a value can also contain '='. 
# • Keep in mind that keys are case sensitive. 
# • The leading and trailing spaces should be removed.
import re
def parse_config(config_file):
    config = {}

    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            match = re.match('^\s*([\w.-]+)\s*=\s*(.*)\s*$', line)
            if match:
                key, value = match.groups()
                config[key] = value
    return config
