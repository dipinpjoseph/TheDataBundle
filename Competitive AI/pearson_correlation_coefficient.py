# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
# Mathematical Explanation - https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

p_s = [ 15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
h_s = [ 10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

mean_p_s = sum(p_s)/len(p_s)
mean_h_s = sum(h_s)/len(p_s)

diff_p_s = [x-mean_p_s for x in p_s]
diff_h_s = [x-mean_h_s for x in h_s]

num = sum([x*y for x,y in zip(diff_p_s,diff_h_s)])
den = ((sum([x**2 for x in diff_p_s]))**0.5)*((sum([x**2 for x in diff_h_s]))**0.5)

pearson_corr_coef = num/den

print(round(pearson_corr_coef,3))

