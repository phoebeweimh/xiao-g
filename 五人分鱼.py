#!/usr/bin/env python
# !coding:utf-8

#A、B、C、D、E 五人合伙捕鱼。A 将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。B C、D、E也按同样的方法拿鱼。问他们至少捕了多少条鱼?
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


if __name__ == '__main__':
    main()