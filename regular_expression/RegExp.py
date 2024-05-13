import re

context="""6 1 10 [Providing Suggestions] I see. Well it's nice that we matched up!
EOS 6 0 11 You're a great resource then! I am majoring in Psychology with a minor in Biology.  """
pattern="\[.+\]"


context=" you to pick me up from college at this time, and you'll have to come by foot :P\" (Note: this sentence contains informal language and unnecessary gossip)"
pattern="\(Note: .+\)"

prog= re.compile(pattern)

# 查找
temp=prog.findall(context)
print(temp)


# 替换
replace_str=' '
result=prog.sub(replace_str,context)
print(result)


# rearch  扫描整个字符串并返回第一个成功的匹配
# match   从头开始匹配

print('===============match=================')

reasoning_completion='1: Identify the given information:\n- Paco had 40 cookies.\n- He ate 5 cookies.\n- He gave 13 cookies to his friend.\n\nStep 2: Determine the operations needed:\n- We need to subtract the number of cookies Paco ate and gave away from the total number of cookies he had.\n\n'
step_1='(?:Step )?1: Identify the given information'   # (?: )  不加入group里
step_2='Step 2: Determine the operations needed'
pattern=rf'^{step_1}:?(.+?){step_2}:?(.+?)$'  # (.+?) ?表示非贪婪匹配

# print(pattern)
matchObj=re.match(pattern, reasoning_completion, re.S)   # .默认匹配除了换行符外的所有字符； 加上 re.S 则可以匹配换行符
print(matchObj)
if matchObj:
    print('group1: ', matchObj.group(1))
    print('group2: ',matchObj.group(2))
