#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
class DetectSquares:

    def __init__(self):
        self.point_to_freq = defaultdict(int) # maps tuple(x, y) to freq
        self.y_to_points = defaultdict(list) # maps axis y to tuple(points) on that axis. only contains unique points


    def add(self, point: List[int]) -> None:
        self.point_to_freq[tuple(point)] += 1

        # only add to y_to_points if it's not there yet
        if self.point_to_freq[tuple(point)] == 1:
            y = point[1]
            self.y_to_points[y].append(tuple(point))
        

    def count(self, point: List[int]) -> int:
        x, y = point

        # calc num squares
        num_squares = 0
        # given point, find all other points on the same y axis
        points_same_y = self.y_to_points[y] # defaultdict returns empty list if key dne
        # try making a square with neighbor
        for neighbor in points_same_y:
            # if neighbor has 0 length with point, skip
            if neighbor[0] == x:
                continue

            n_x, n_y = neighbor
            x_dst = n_x - x


            # from neighbor, try find if [n_x, y + x_dst] & [n_x, y - x_dst]
            if tuple([n_x, y + x_dst]) in self.point_to_freq and tuple([x, y + x_dst]) in self.point_to_freq:
                # found a square, find num of squares we can make
                num_squares += (
                    self.point_to_freq[tuple([n_x, n_y])] *
                    self.point_to_freq[tuple([n_x, y + x_dst])] *
                    self.point_to_freq[tuple([x, y + x_dst])]
                )
                
            if tuple([n_x, y - x_dst]) in self.point_to_freq and tuple([x, y - x_dst]) in self.point_to_freq:
                num_squares += (
                    self.point_to_freq[tuple([n_x, n_y])] *
                    self.point_to_freq[tuple([n_x, y - x_dst])] *
                    self.point_to_freq[tuple([x, y - x_dst])]
                )

        return num_squares
        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

