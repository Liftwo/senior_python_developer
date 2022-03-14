class Google_Phone:
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    def special_feature(self, int_list):
        ans = []
        for i in int_list:
            if i%2==0 and i>10:
                ans.append(i)
        return ans


obj_google = Google_Phone(10,3,5)
print(obj_google.special_feature([3, 43, 62, 15, 18, 22]))


class Taiwan_Phone:
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    def special_feature(self, num):
        f = []
        for i in range(num):
            if i<=1:
                f.append(i)
            else:
                f.append(f[-1]+f[-2])
        return f


obj_taiwan = Taiwan_Phone(20,1,3)
print(obj_taiwan.special_feature(10))