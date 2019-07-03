import numpy as np

class Brick:
    def __init__(self,size,n):
        oneArr=np.ones((1,n))
        zeroArr=np.zeros((1,size[0]*size[1]-n))
        self.brickArray=np.append(oneArr,zeroArr) #值为1表示有雷
        np.random.shuffle(self.brickArray)
        self.brickArray=self.brickArray.astype(int).reshape(size)#得到只有雷的矩阵
        #设置数字数组——非边缘
        arr=np.zeros(self.brickArray.shape,dtype=int)
        for i in range(0,self.brickArray.shape[0]):
            for j in range(0,self.brickArray.shape[1]):
                if(self.brickArray[i,j]==0):
                    #四个角落的值
                    if(i==0 and j==0):
                        arr[i,j]=self.brickArray[i,j+1]+self.brickArray[i+1,j]+self.brickArray[i+1,j+1]
                    elif(i==self.brickArray.shape[0]-1 and j==0):
                        arr[i,j]=self.brickArray[i-1,j]+self.brickArray[i,j+1]+self.brickArray[i-1,j+1]
                    elif(i==0 and j==self.brickArray.shape[1]-1):
                        arr[i,j]=self.brickArray[i,j-1]+self.brickArray[i+1,j]+self.brickArray[i+1,j-1]
                    elif(i==self.brickArray.shape[0]-1 and j==self.brickArray.shape[1]-1):
                        arr[i,j]=self.brickArray[i,j-1]+self.brickArray[i-1,j]+self.brickArray[i-1,j-1]
                    #四个边缘的值
                    elif(i==0):
                        arr[i,j]=self.brickArray[i,j-1]+self.brickArray[i,j+1]+self.brickArray[i+1,j-1]+self.brickArray[i+1,j]+self.brickArray[i+1,j+1]
                    elif(i==self.brickArray.shape[0]-1):
                        arr[i,j]=self.brickArray[i-1,j-1]+self.brickArray[i-1,j]+self.brickArray[i-1,j+1]+self.brickArray[i,j-1]+self.brickArray[i,j+1]
                    elif(j==0):
                        arr[i,j]=self.brickArray[i-1,j]+self.brickArray[i-1,j+1]+self.brickArray[i,j+1]+self.brickArray[i+1,j]+self.brickArray[i+1,j+1]
                    elif(j==self.brickArray.shape[1]-1):
                        arr[i,j]=self.brickArray[i-1,j-1]+self.brickArray[i-1,j]+self.brickArray[i,j-1]+self.brickArray[i+1,j-1]+self.brickArray[i+1,j]
                    else:
                        arr[i,j]=self.brickArray[i-1,j-1]+self.brickArray[i-1,j]+self.brickArray[i-1,j+1]+self.brickArray[i,j-1]+\
                            self.brickArray[i,j+1]+self.brickArray[i+1,j-1]+self.brickArray[i+1,j]+self.brickArray[i+1,j+1]
        self.brickArray=self.brickArray*10+arr
        self.OpenFlagArr=np.zeros((self.brickArray.shape[0],self.brickArray.shape[1]),dtype=int)

    def isNoBomb(self,pos):
        i=pos[0]
        j=pos[1]
        brickPosList=[]        
        #四个角落的值
        if(i==0 and j==0):
            brickPosList.append((i,j+1))
            brickPosList.append((i+1,j))
            brickPosList.append((i+1,j+1))
        elif(i==self.brickArray.shape[0]-1 and j==0):
            brickPosList.append((i-1,j))
            brickPosList.append((i,j+1))
            brickPosList.append((i-1,j+1))
        elif(i==0 and j==self.brickArray.shape[1]-1):
            brickPosList.append((i,j-1))
            brickPosList.append((i+1,j-1))
            brickPosList.append((i+1,j))
        elif(i==self.brickArray.shape[0]-1 and j==self.brickArray.shape[1]-1):
            brickPosList.append((i,j-1))
            brickPosList.append((i-1,j))
            brickPosList.append((i-1,j-1))
        #四个边缘的值
        elif(i==0):
            brickPosList.append((i,j-1))
            brickPosList.append((i,j+1))
            brickPosList.append((i+1,j-1))
            brickPosList.append((i+1,j))
            brickPosList.append((i+1,j+1))
        elif(i==self.brickArray.shape[0]-1):
            brickPosList.append((i-1,j-1))
            brickPosList.append((i-1,j))
            brickPosList.append((i-1,j+1))
            brickPosList.append((i,j-1))
            brickPosList.append((i,j+1))
        elif(j==0):
            brickPosList.append((i-1,j))
            brickPosList.append((i-1,j+1))
            brickPosList.append((i,j+1))
            brickPosList.append((i+1,j))
            brickPosList.append((i+1,j+1))
        elif(j==self.brickArray.shape[1]-1):
            brickPosList.append((i-1,j-1))
            brickPosList.append((i-1,j))
            brickPosList.append((i,j-1))
            brickPosList.append((i+1,j-1))
            brickPosList.append((i+1,j))
        else:
            brickPosList.append((i-1,j-1))
            brickPosList.append((i-1,j))
            brickPosList.append((i-1,j+1))
            brickPosList.append((i,j-1))
            brickPosList.append((i,j+1))
            brickPosList.append((i+1,j-1))
            brickPosList.append((i+1,j))
            brickPosList.append((i+1,j+1))
        return self.checkSame(brickPosList)

    def checkSame(self,brickPosList):
        flag=True
        for p in brickPosList:
            if(self.brickArray[p[0],p[1]]==10 and self.OpenFlagArr[p[0],p[1]]!=2):
                flag=False
        return flag

    def isVictory(self):
        flag=True
        rows=self.brickArray.shape[0]
        cols=self.brickArray.shape[1]
        for i in range(rows):
            for j in range(cols):
                if(self.brickArray[i,j]==10 and self.OpenFlagArr[i,j]!=2):
                    flag=False
                elif(self.OpenFlagArr[i,j]==2 and self.brickArray[i,j]!=10):
                    flag=False
        return flag

    def getSurplusNumber(self):
        n=0
        rows=self.brickArray.shape[0]
        cols=self.brickArray.shape[1]
        for i in range(rows):
            for j in range(cols):
                if(self.brickArray[i,j]==10 and self.OpenFlagArr[i,j]==0):
                    n=n+1
        return n

    def getBrickArr(self):
        return self.brickArray


