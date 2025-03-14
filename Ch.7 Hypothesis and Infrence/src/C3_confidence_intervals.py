# 3a) "Confidence Intervals" Ex: 525 heads / 1000 flips = p == 0.525
import math
p_hat = 525 / 1000
mu = p_hatsigma = math.sqrt(p_hat * (1 - p_hat) / 1000)  # 0.0158

# "We are 95% confident that the following interval contains the true parameter p":
from A1_flipping_a_coin import normal_two_sided_bounds
mu = 0
sigma = 1
normal_two_sided_bounds(0.95, mu, sigma)

# If it was heads 540 times:
p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158
normal_two_sided_bounds(0.95, mu, sigma) # [0.5091, 0.5709]