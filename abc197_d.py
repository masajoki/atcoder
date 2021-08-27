import math
import numpy as np

N=int(input())
x0,y0=map(int,input().split())
xe,ye=map(int,input().split())

xdif=x0-xe
ydif=y0-ye

base_point=np.array([x0-xdif, y0-ydif])

kakudo=360/N
rad=math.radians(kakudo)


def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
    return rot

rot=get_rotation_matrix(rad)
rotated=np.dot(rot,base_point)
dif=np.array([xdif,ydif])

ans=rotated+dif
print(ans[0],ans[1])