#アルゴ式.データ全体の補正 (線形変換).py
savg,sstd,seppen,katamuki=map(int,input().split())

print(savg*katamuki+seppen,sstd*katamuki)
