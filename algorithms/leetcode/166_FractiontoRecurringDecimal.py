class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        4
        333
        1.4*100 400/333  1, 67
        2.67*10 670/333  2, 4
        3.4*100 400/333, 1
        
        
       
        
        """
        d = denominator
        dvdn_set = {}
        fra = []
        cir_strt = None

        def rec_div(n):
            nonlocal cir_strt
            if n in dvdn_set:  # circle
                if not cir_strt:
                    cir_strt = n
                return
            dvdn_set[n] = len(fra)
            # print(dvdn_set)
            if n < d:
                n *= 10
                if n < d:
                    fra.append('0')
                rec_div(n)
            else:
                q = n // d
                fra.append(str(q))
                r = n % d
                if r > 0:
                    rec_div(r)

        qt, re = divmod(abs(numerator), abs(d))
        sign = '-' if numerator * d < 0 else ''
        numerator, d = abs(numerator), abs(d)
        # print(qt, re)
        if re > 0:
            rec_div(re)
            # print('fra',fra)
            # print('cir_strt',cir_strt)
            if cir_strt:
                #insert (), like .7(263)
                # print('dvdn_set',dvdn_set)
                for i in range(len(fra)):
                    if i == dvdn_set[cir_strt]:
                        # print('add ()', i)
                        fra = fra[:i] + ['('] + fra[i:] + [')']
                        # print(fra)
                        break
            ans = str(qt)+'.'+''.join(fra)
        else:
            ans = str(qt)

        return sign+ans
