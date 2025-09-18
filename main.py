# 在这个文件里编写代码
weight = float(input())
increase = 0.5
moon_ratio = 0.165

for year in range(1, 11):
    earth = weight + increase * year
    moon = earth * moon_ratio
    print(f"{year} {earth:.1f} {moon:.2f}")
