#渡されたファイルと，それを修正したファイルをバイナリモードで読み込む
with open('DifferenceTest.java','rb') as f1, open('DifferenceTest1.java','rb') as f2:
    #bf1,bf2はbytes型
    bf1=f1.read()
    bf2=f2.read()
    #bytearrayはbytesと同じようなものだけど，bytesと違って値の変更が可能
    btext=bytearray([])
    #以下では渡されたファイル（所々に文字として読み込めない値がある）と適切に動作するように変更を加えたファイルの差分
    #(正確には文字として認識されない部分と，本来あるべき文字のasciiコードの差分)をとる．
    try:
        for i in range(len(bf1)):
            if bf1[i]!=bf2[i]:
                diff=bf1[i]-bf2[i]
                if diff==0:
                    #比較している部分が同じならば何もしない
                    None
                elif diff<0:
                    #比較している部分が異なり，さらに上のdiffの式で得られた差分が負であれば正にしてbtext変数に追加
                    btext.append(diff*-1)
                else:
                    #比較している部分が異なれば，その差分をbtext変数に追加
                    btext.append(diff)
    except IndexError:
        None
    #btextをbytearrayからStringに戻せばフラグが得られる．
    print('Flag is \''+btext.decode()+'\'')
