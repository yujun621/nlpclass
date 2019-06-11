#!/usr/bin/env python
# coding: utf-8

# ### 예외처리
# 프로그램을 실행하다 발생하는 오류

# In[1]:


print(10/0)


# In[2]:


try:
    print(10/0)
except:
    print("예외오류발생")#오류발생시 코드


# 특정예외만 처리

# In[6]:


x = [1, 2, 3]
try:
    print(10/0)
    x[5]
except ZeroDivisionError as e:
    print("숫자를 0으로 나눌 수 없음", e)
except IndexError as e:
    print("잘못된 인덱스", e)


# In[7]:


try:
    x[5]
except IndexError as e:
    print("잘못된 인덱스", e)


# #### 예외처리 else와 finally
# 
# else: 오류가 발생하지 않을때만 동작
# finally: 오류발생여부 상관없이 무조건 동작

# In[8]:


try:
    print(10/0)
except:
    print("예외오류발생")
else:
    print("오류발생하지 않음")
finally:
    print("무조건 실행")


# ### 예외 발생시키기 raise

# In[9]:


try:
    raise Exception("예외강제발생")
except Exception as e:
    print("예외발생",e)


# In[10]:


class MyError(Exception):
    def __init__(self):
        super().__init__("나의오류")

try:
    raise MyError
except Exception as e:
    print("예외발생",e)


# In[ ]:




