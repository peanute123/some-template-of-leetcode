# coding=utf-8
import win32api
import win32con
import win32gui

def move(x, y):
  """
  函数功能：移动鼠标到指定位置
  参  数：x:x坐标
       y:y坐标
  """
  win32api.SetCursorPos((x, y))


def get_cur_pos():
  """
  函数功能：获取当前鼠标坐标
  """
  p={"x":0,"y":0}
  pos = win32gui.GetCursorPos()
  p['x']=pos[0]
  p['y']=pos[1]
  return p


def left_click():
  """
  函数功能：鼠标左键点击
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click():
  """
  函数功能：鼠标右键点击
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def left_down():
  """
  函数功能：鼠标左键按下
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def left_up():
  """
  函数功能：鼠标左键抬起
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_down():
  """
  函数功能：鼠标右键按下
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def right_up():
  """
  函数功能：鼠标右键抬起
  """
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
  
import time 
if __name__ == '__main__':
    fang = (1219,541) #防的位置
    ans = [1,0,0,2,1,
           2,1,1,2,0,
           0,1,2,1,0]
    xy = [(500,855),(500,890),(500,925) ] #选项的位置
    time.sleep(4)
    epoch = 3
    for epo in range(epoch):#想刷的次数
        for i in range(15): 
            if i==0 or i==14:#最后一题时间有点长
                for _ in range(3):
                    move(*fang) 
                    left_click() 
                    time.sleep(1.)
            for _ in range(8):
                move(*fang)
                left_click()
                time.sleep(1.)
            move( *(xy[ans[i]]) )
            left_click()
            time.sleep(2)
        move( *fang )
        left_click()   
        if epo == epoch-1:break
        time.sleep( 171 )#站着别动，重新刷出来
        right_click()
        time.sleep( 171 )#防止电脑熄屏
        move(*fang)#防止鼠标被移动到攻
        left_click()
          