class Solution(object):
    def main(self, a):
        sum = 0
        for item in a:
            sum += int(item)
        return sum


if __name__ == "__main__":
    print(Solution().main("1623552460048932486847030"))
