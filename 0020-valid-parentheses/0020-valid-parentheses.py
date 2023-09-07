class Solution:
    def isValid(self, ss: str) -> bool:
        st = []
        opened = ['(', '{', '[']
        for s in ss:
            if not st or s in opened:
                st.append(s)
                continue
            if s == ')':
                if st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif s == '}':
                if st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif s == ']':
                if st[-1] == '[':
                    st.pop()
                else:
                    return False
        
        if not st:
            return True