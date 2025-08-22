class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
            start = {}
            for i in range(len(phrases)):
                words = list(phrases[i].split(" "))
                sw,ew = words[0],words[-1]
                if sw in start:
                    start[sw].append(i)
                else:
                    start[sw] = [i]
                
                
            #print (start)
            res = []
            seen = set()
            for i in range(len(phrases)):
                ew = list(phrases[i].split(" "))[-1]    
                if ew in start:
                    for j in start[ew]:
                        if i!=j:
                            string = phrases[i]+phrases[j][len(ew):]
                            if string in seen:
                                continue
                            else:
                                res.append(string)
                                seen.add(string)
            return sorted(res)
