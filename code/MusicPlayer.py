# 簡易音樂播放器
import os
import pygame
import random
import wx
import time

volume = [0.1]
sum = [1]
musicUrlList = []
#加载音樂目錄下的所有.mp3文件加進陣列備用
def musicUrlLoader():
    fileList = os.listdir("./music/")
    for filename in fileList:
        if filename.endswith(".mp3"):
            print("找到音频文件",filename)      
            musicUrlList.append(filename)
            
    return fileList
#建立MyMusicPlayer的類別並繼承wx.frame
class MyMusicPlayer(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent = superion, title = 'MP3 Player',size = (400,300))

        musicUrlLoader()
        #創建面板
        MainPanel = wx.Panel(self)
        #面板背景色
        MainPanel.SetBackgroundColour('pink')
        #顯示音樂
        self.ShowInfoText = wx.StaticText(parent = MainPanel, label = '播放未開始', pos = (100,100)
                                          ,size = (185,25),style = wx.ALIGN_CENTER_VERTICAL)
        self.ShowInfoText.SetBackgroundColour('white')

        self.isPaused = True   #是否被暂停
        #音樂撥放
        self.StartPlayButton = wx.Button(parent = MainPanel, label = '隨機播放', pos = (100,130))
        self.Bind(wx.EVT_BUTTON, self.OnStartClicked, self.StartPlayButton)
        #音樂暫停
        self.PauseOrContinueButton = wx.Button(parent = MainPanel, label = '暂停播放', pos = (200,130))
        self.Bind(wx.EVT_BUTTON, self.OnPauseOrContinueClicked, self.PauseOrContinueButton)
        self.PauseOrContinueButton.Enable(True)
        #"音量鍵"文字類型
        font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, 'Arial')
        
        self.ShowF = wx.StaticText(parent = MainPanel, label = '功能鍵:', pos = (10,130)
                                          ,size = (50,100),style = wx.ALIGN_CENTER_VERTICAL)
        #顯示音量鍵(文字)
        self.ShowVolume = wx.StaticText(parent = MainPanel, label = '音量鍵:', pos = (10,170)
                                          ,size = (50,100),style = wx.ALIGN_CENTER_VERTICAL)
        self.ShowVolume.SetFont(font)
        self.ShowF.SetFont(font)
        
        self.ShowInfoText.SetBackgroundColour('white')
        #音量鍵功能(按鈕)
        self.VolumeUP = wx.Button(parent = MainPanel, label = '+', pos = (100,170))
        self.Bind(wx.EVT_BUTTON, self.VolumeUPfunc,self.VolumeUP)
        
        self.VolumeDOWN = wx.Button(parent = MainPanel, label = '-', pos = (200,170))
        self.Bind(wx.EVT_BUTTON, self.VolumeDOWNfunc,self.VolumeDOWN)
        
        pygame.mixer.init()
        
        

        
    def VolumeUPfunc(self,event):
        n = volume[0]
        volume.remove(n)
        n += 0.1
        volume.append(n)
        pygame.mixer.music.set_volume(n)

    
    def VolumeDOWNfunc(self,event):
        n = volume[0]
        volume.remove(n)
        n -= 0.1
        volume.append(n)
        pygame.mixer.music.set_volume(n)


    def OnStartClicked(self,event):
        fileList = musicUrlLoader()
        
        self.isPaused = True
        self.PauseOrContinueButton.Enable(True)
        self.willPlayMusic =  random.choice(musicUrlList)
        n = volume[0]
        pygame.mixer.music.set_volume(n)
        pygame.mixer.music.load('./music/'+self.willPlayMusic)  
        pygame.mixer.music.play()

        self.ShowInfoText.SetLabel("当前播放:"+self.willPlayMusic)
    def OnPauseOrContinueClicked(self,event):
        if not self.isPaused:
            self.isPaused = True
            pygame.mixer.music.pause()
            
            self.PauseOrContinueButton.SetLabel('继续播放')

            self.ShowInfoText.SetLabel('播放已暂停')
        else:
            self.isPaused = False
            pygame.mixer.music.unpause()
            self.PauseOrContinueButton.SetLabel('暂停播放')

            self.ShowInfoText.SetLabel("当前播放:" + self.willPlayMusic)


if __name__ == "__main__":
    app = wx.App()
    myMusicPlayer = MyMusicPlayer(None)
    myMusicPlayer.Show()
    app.MainLoop()
