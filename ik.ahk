SetCapsLockState, AlwaysOff
SetTitleMatchMode, 2

^#R:: Reload Return  ;오토핫키 재실행
^#E:: Edit Return ;오토핫키 편집하기
^#p:: Run, "C:\Users\home\Documents\03.Utility\0.utility\AU3_Spy.exe" Return ;AU3_Spy실행
;end:: exitapp ;오토핫키 종료

;프로그램 실행
^#t::Run "C:\Users\home\AppData\Roaming\Telegram Desktop\Telegram.exe"
^#k::Run "C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
^#s::Run "C:\Program Files\Google\Chrome\Application\chrome.exe" https://docs.google.com/spreadsheets/u/0/
^#m::Run "C:\Program Files\Google\Chrome\Application\chrome.exe" https://mail.google.com
^#c::Run "C:\Program Files\Google\Chrome\Application\chrome.exe"
^#b::Run "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" https://www.google.com
^#0::Run "C:\iktools\CloseAll.exe"
^#NumpadSub::Run "%windir%\System32\rundll32.exe" powrprof.dll SetSuspendState
^esc::Run "%windir%\System32\rundll32.exe" powrprof.dll SetSuspendState
^#z::Run "C:\Program Files (x86)\Ditto\Ditto.exe" /open

!space::
Run "C:\Program Files\Everything\Everything.exe"
return

!XButton1::
send, !{f4}
return

^XButton1::
send, ^{w}
return

NumpadSub::
send, +{-}
return

;상용구 실행

:*:nm_+::
clipboard := "map.naver.com"
send ^v
return

:*:ahs``::
clipboard := "몬스터헌터"
send ^v
return

:*:la^?::
clipboard := "lavastar"
send ^v
send {Tab}
clipboard := "cd03pd81"
send ^v{enter}
return

:*:tmg_+::
clipboard := "tmasterk@gmail.com"
send ^v
return

#If GetKeyState("Capslock","P")
    W::
    q::
    click 114 66
    sleep 500
    click 126 203
    return
    r::
    click 415 874
    sleep 2000
    click 1582 1010
    sleep 3500
    click 411 291,2
    sleep 1000
    click 866 605
    v:: run, %windir%\System32\SndVol.exe -f 49825268
    return
