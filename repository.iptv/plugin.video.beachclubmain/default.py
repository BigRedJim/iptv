# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import xbmcplugin , xbmcgui , xbmc , xbmcaddon
import sys , requests , re , os , urllib , time , urllib2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.beachclubmain'
oo = xbmcaddon . Addon ( id = o0OO00 )
i1iII1IiiIiI1 = xbmc . translatePath ( 'special://home/addons/' + str ( o0OO00 ) + '/' )
iIiiiI1IiI1I1 = oo . getSetting ( 'folder' )
o0OoOoOO00 = os . path . join ( i1iII1IiiIiI1 , 'm3ucache' )
if not os . path . exists ( o0OoOoOO00 ) :
 os . makedirs ( o0OoOoOO00 )
I11i = os . path . join ( o0OoOoOO00 , 'temp.m3u' )
O0O = os . path . join ( i1iII1IiiIiI1 , 'm3ucache' , 'logo.txt' )
Oo = os . path . join ( i1iII1IiiIiI1 , 'icon.png' )
I1ii11iIi11i = os . path . join ( i1iII1IiiIiI1 , 'fanart.jpg' )
I1IiI = oo . getSetting ( 'username' )
o0OOO = oo . getSetting ( 'password' )
iIiiiI = xbmcgui . Dialog ( )
Iii1ii1II11i = xbmcgui . DialogProgress ( )
iI111iI = 'service.xbmc.beachclubmain'
IiII = xbmc . translatePath ( 'special://home/userdata/addon_data/' + str ( iI111iI ) + '/' )
iI1Ii11111iIi = os . path . join ( IiII , 'awaiting_download.txt' )
i1i1II = os . path . join ( IiII , 'series_link.txt' )
if not os . path . exists ( iI1Ii11111iIi ) :
 open ( iI1Ii11111iIi , 'w+' )
if not os . path . exists ( i1i1II ) :
 open ( i1i1II , 'w+' )
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
o0oOoO00o = oo . getSetting ( "epg" )
if 43 - 43: O0OOo . II1Iiii1111i
i1IIi11111i = 'http://theonetv.vip/get.php?username=' + I1IiI + '&password=' + o0OOO + '&type=m3u_plus&output=ts'
o000o0o00o0Oo = 'http://theonetv.vip/xmltv.php?username=' + I1IiI + '&password=' + o0OOO + '&type=m3u_plus&output=ts'
if 80 - 80: i1iII1I1i1i1 . i1iIIII
def I1 ( name ) :
 O0OoOoo00o = name . replace ( ' ' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '-' , '' ) [ - 8 : ]
 O0OoOoo00o = O0OoOoo00o [ - 4 : ] + O0OoOoo00o [ : 4 ]
 name = name [ : - 13 ] + O0OoOoo00o
 iiiI11 = os . path . join ( iIiiiI1IiI1I1 , name + '.mp4' )
 os . remove ( iiiI11 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 91 - 91: oOOOO / i1iiIII111ii + iiIIi1IiIi11 . i1Ii
def I111I11 ( name ) :
 O0O00Ooo = [ ]
 OOoooooO = ''
 with open ( i1i1II ) as i1iIIIiI1I :
  for OOoO000O0OO , iiI1IiI in enumerate ( i1iIIIiI1I ) :
   if name in iiI1IiI :
    pass
   else :
    O0O00Ooo . append ( iiI1IiI )
 for iiI1IiI in O0O00Ooo :
  OOoooooO += iiI1IiI
 i1iIIIiI1I . close ( )
 if OOoooooO != '' :
  II = open ( i1i1II , 'w+' )
  II . write ( OOoooooO )
  II . close ( )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 57 - 57: ooOoo0O
def OooO0 ( name ) :
 II11iiii1Ii = open ( I11i ) . read ( )
 II11iiii1Ii = II11iiii1Ii . replace ( '>USERNAME<' , I1IiI ) . replace ( '>PASSWORD<' , o0OOO )
 OO0o = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , II11iiii1Ii )
 for Ooo , O0o0Oo in OO0o :
  O0o0Oo = O0o0Oo . strip ( )
  Oo00OOOOO = re . findall ( 'name="(.+?)"' , Ooo ) [ 0 ]
  O0OO00o0OO = re . findall ( 'tvg-logo="(.+?)"' , Ooo ) [ 0 ]
  try :
   I11i1 = re . findall ( 'group-title="(.+?)"' , Ooo ) [ 0 ]
  except :
   I11i1 = ''
  try :
   if I11i1 == name :
    iIi1ii1I1 ( Oo00OOOOO , O0o0Oo , 9 , O0OO00o0OO , '' , '' )
  except Exception as o0 :
   pass
   if 9 - 9: oOOOO + II1Iiii1111i % oOOOO + i1IIi . i1iII1I1i1i1
def III1i1i ( name ) :
 O0O00Ooo = [ ]
 OOoooooO = ''
 iiI1 = 1000
 with open ( iI1Ii11111iIi ) as i1iIIIiI1I :
  for OOoO000O0OO , iiI1IiI in enumerate ( i1iIIIiI1I ) :
   if name [ 14 : ] in iiI1IiI :
    iiI1 = int ( OOoO000O0OO )
   if int ( OOoO000O0OO ) == iiI1 + 2 and 'hour_to_start' in iiI1IiI :
    if name [ 9 : 10 ] in iiI1IiI :
     iiI1 = int ( OOoO000O0OO )
   if int ( OOoO000O0OO ) == iiI1 + 1 and 'minute_to_start' in iiI1IiI :
    if name [ 12 : 13 ] in iiI1IiI :
     iiI1 = int ( OOoO000O0OO )
   if int ( OOoO000O0OO ) == iiI1 + 4 and 'day' in iiI1IiI :
    if name [ : 2 ] in iiI1IiI :
     iiI1 = int ( OOoO000O0OO )
   if int ( OOoO000O0OO ) == iiI1 + 1 and 'month' in iiI1IiI :
    if name [ 3 : 5 ] in iiI1IiI :
     iiI1 = int ( OOoO000O0OO )
 if iiI1 != 1000 :
  with open ( iI1Ii11111iIi ) as i1iIIIiI1I :
   for OOoO000O0OO , iiI1IiI in enumerate ( i1iIIIiI1I ) :
    if OOoO000O0OO in range ( iiI1 - 9 , iiI1 + 2 ) :
     pass
    else :
     OOoooooO += iiI1IiI
  i1iIIIiI1I . close ( )
 if OOoooooO != '' :
  II = open ( iI1Ii11111iIi , 'w+' )
  II . write ( OOoooooO )
  II . close ( )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 19 - 19: i1iIIII + ooOoo0O
def ooo ( ) :
 iI1Ii11111iIi = os . path . join ( IiII , 'awaiting_download.txt' )
 ii1I1i1I = open ( iI1Ii11111iIi ) . read ( )
 OOoo0O0 = re . findall ( '<programme>(.+?)</programme>' , str ( ii1I1i1I ) , re . DOTALL )
 for iiiIi1i1I in OOoo0O0 :
  oOO00oOO = re . findall ( '<name>(.+?)</name>' , iiiIi1i1I ) [ 0 ]
  OoOo = re . findall ( '<download_link>(.+?)</download_link>' , iiiIi1i1I ) [ 0 ]
  iI = re . findall ( '<hour_to_start>(.+?)</hour_to_start>' , iiiIi1i1I ) [ 0 ]
  o00O = re . findall ( '<minute_to_start>(.+?)</minute_to_start>' , iiiIi1i1I ) [ 0 ]
  OOO0OOO00oo = re . findall ( '<hour_to_end>(.+?)</hour_to_end>' , iiiIi1i1I ) [ 0 ]
  Iii111II = re . findall ( '<minute_to_end>(.+?)</minute_to_end>' , iiiIi1i1I ) [ 0 ]
  iiii11I = re . findall ( '<duration>(.+?)</duration>' , iiiIi1i1I ) [ 0 ]
  Ooo0OO0oOO = re . findall ( '<day>(.+?)</day>' , iiiIi1i1I ) [ 0 ]
  ii11i1 = re . findall ( '<month>(.+?)</month>' , iiiIi1i1I ) [ 0 ]
  IIIii1II1II = Ooo0OO0oOO + '/' + ii11i1 + ' - ' + iI + ':' + o00O
  iIi1ii1I1 ( IIIii1II1II + ' ' + oOO00oOO , '' , 1001 , '' , '' , '' )
  if 42 - 42: oOOOO + II1Iiii1111i
def o0O0o0Oo ( ) :
 iIi1ii1I1 ( 'Recorded shows' , '' , 1000 , '' , '' , '' )
 try :
  Ii11Ii1I = str ( xbmc . getInfoLabel ( 'System.FreeSpace' ) )
  O00oO = int ( Ii11Ii1I . replace ( ' MB' , '' ) . replace ( ' Free' , '' ) )
  if O00oO < 2000 :
   iIi1ii1I1 ( 'You have under 2gb of storage left, It is advisable that you set storage location' , '' , 1000 , '' , '' , '' )
   iIi1ii1I1 ( 'to an external source or you run the risk of causing issue to your device' , '' , 1000 , '' , '' , '' )
  iIi1ii1I1 ( Ii11Ii1I , '' , 1000 , '' , '' , '' )
 except :
  pass
 for I11i1I1I in os . walk ( iIiiiI1IiI1I1 ) . next ( ) [ 2 ] :
  if '.mp4' in I11i1I1I :
   oO0Oo = I11i1I1I . replace ( '.mp4' , '' )
   IIIii1II1II = oO0Oo [ : - 8 ] + oO0Oo [ - 4 : - 2 ] + '/' + oO0Oo [ - 2 : ] + ' - ' + oO0Oo [ - 8 : - 6 ] + ':' + oO0Oo [ - 6 : - 4 ]
   iIi1ii1I1 ( IIIii1II1II , os . path . join ( iIiiiI1IiI1I1 , I11i1I1I ) , 16 , '' , '' , '' , '' )
   if 54 - 54: Oo0oO0ooo - Oo0ooO0oo0oO + OoooooooOO
def O0o0 ( name , url ) :
 O0o0 = True
 if not os . path . exists ( IiII ) :
  os . makedirs ( IiII )
 if not os . path . exists ( i1i1II ) :
  OO00Oo = open ( i1i1II , "w+" )
  OO00Oo . close ( )
 ii1I1i1I = open ( i1i1II ) . read ( )
 if ii1I1i1I != '' :
  O0OOO0OOoO0O = re . findall ( '<name>(.+?)</name>' , ii1I1i1I )
  for O00Oo000ooO0 in O0OOO0OOoO0O :
   if O00Oo000ooO0 == name :
    O0o0 = False
   else :
    pass
 if O0o0 == True or O0o0 == False :
  OoO0O00 = open ( i1i1II , "a+" )
  name = name . replace ( '  ' , '' )
  OoO0O00 . write ( '<name>' + name + '</name><url>' + url + '</url>\n' )
 else :
  pass
  if 5 - 5: I1i1iI1i / Oo0oO0ooo . oOOOO - O0 / iiIIi1IiIi11
def ooOooo000oOO ( ) :
 iIi1ii1I1 ( 'Series Links' , '' , 1000 , '' , '' , '' )
 i1i1II = os . path . join ( IiII , 'series_link.txt' )
 OoO0O00 = open ( i1i1II ) . read ( )
 Oo0oOOo = re . findall ( '<name>(.+?)</name><url>(.+?)</url>' , OoO0O00 )
 for oOO00oOO , Oo0OoO00oOO0o in Oo0oOOo :
  try :
   oOO00oOO = oOO00oOO . split ( '- ' ) [ 1 ] . split ( ' *' ) [ 0 ]
  except :
   oOO00oOO = oOO00oOO . split ( '| ' ) [ 1 ] . split ( ' *' ) [ 0 ]
  finally :
   oOO00oOO = oOO00oOO
  iIi1ii1I1 ( oOO00oOO , Oo0OoO00oOO0o , 1000 , '' , '' , '' )
  if 80 - 80: II1Iiii1111i + i1iII1I1i1i1 - i1iII1I1i1i1 % i1iiIII111ii
  if 63 - 63: Oo0ooO0oo0oO - O0OOo + O0 % i1iIIII / iIii1I11I1II1 / Oo0oO0ooo
def O0o0O00Oo0o0 ( ) :
 iIi1ii1I1 ( 'Search Channel' , '' , 4 , '' , '' , '' )
 iIi1ii1I1 ( 'Categories' , '' , 10 , '' , '' , '' )
 iIi1ii1I1 ( 'Full List' , '' , 1 , '' , '' , '' )
 iIi1ii1I1 ( 'My Recorded Shows' , '' , 7 , '' , '' , '' )
 iIi1ii1I1 ( 'Schedule Recordings' , '' , 10 , '' , '' , '' )
 iIi1ii1I1 ( 'View Recordings' , '' , 11 , '' , '' , '' )
 iIi1ii1I1 ( 'View Series Links' , '' , 14 , '' , '' , '' )
 iIi1ii1I1 ( 'Update Channel List' , '' , 3 , '' , '' , '' )
 if 87 - 87: ooOoo0O * I1i1iI1i % i11iIiiIii % o00 - i1iII1I1i1i1
 if 68 - 68: i1Ii % i1IIi . iiIIi1IiIi11 . O0OOo
def o0oo0oOo ( name ) :
 o000O0o = [ ]
 II11iiii1Ii = open ( I11i ) . read ( )
 II11iiii1Ii = II11iiii1Ii . replace ( '>USERNAME<' , I1IiI ) . replace ( '>PASSWORD<' , o0OOO )
 OO0o = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , II11iiii1Ii )
 for Ooo , O0o0Oo in OO0o :
  try :
   iI1iII1 = re . findall ( 'group-title="(.+?)"' , Ooo ) [ 0 ]
   if iI1iII1 not in str ( o000O0o ) :
    o000O0o . append ( iI1iII1 )
  except :
   pass
 for oO0OOoo0OO in o000O0o :
  if name == 'Categories' :
   try :
    iIi1ii1I1 ( oO0OOoo0OO , '' , 1 , '' , '' , '' )
   except :
    pass
  if name == 'Schedule Recordings' :
   try :
    iIi1ii1I1 ( oO0OOoo0OO , '' , 8 , '' , '' , '' )
   except :
    pass
    if 65 - 65: oOOOO . iIii1I11I1II1 / O0 - oOOOO
    if 21 - 21: Oo0ooO0oo0oO * iIii1I11I1II1
    if 91 - 91: iiIIi1IiIi11
def iiIii ( name ) :
 ooo0O = oOoO0o00OO0 ( )
 if ':' in name :
  i1I1ii , oOOo0 , oo00O00oO , iIiIIIi = re . findall ( '\*(.+?)/(.+?) (.+?):(.+?)\*' , name ) [ 0 ]
 try :
  name = name . split ( '- ' ) [ 1 ] . split ( ' *' ) [ 0 ]
 except :
  name = name . split ( '| ' ) [ 1 ] . split ( ' *' ) [ 0 ]
 while name [ - 1 ] == ' ' :
  name = name [ : - 1 ]
 Oo0oOOo = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , ooo0O , re . DOTALL )
 for ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo in Oo0oOOo :
  try :
   ooOOO00Ooo = ooOOO00Ooo . replace ( '<' , '' )
   if name . encode ( 'UTF-8' ) in oo0OOo . encode ( 'UTF-8' ) :
    ii11i1 = ooo00OOOooO [ 4 : 6 ] ; Ooo0OO0oOO = ooo00OOOooO [ 6 : 8 ] ; iI = ooo00OOOooO [ 8 : 10 ]
    o00O = ooo00OOOooO [ 10 : 12 ] ; OOO0OOO00oo = O00OOOoOoo0O [ 8 : 10 ] ; Iii111II = O00OOOoOoo0O [ 10 : 12 ] ; name = name
    if ii11i1 == oOOo0 and Ooo0OO0oOO == i1I1ii :
     if iI == oo00O00oO and o00O == iIiIIIi :
      IiIIIi1iIi = int ( ooo00OOOooO [ 8 : 12 ] )
      ooOOoooooo = int ( O00OOOoOoo0O [ 8 : 12 ] )
      iiii11I = ooOOoooooo - IiIIIi1iIi
      if O00OOOoOoo0O [ 8 : 10 ] > ooo00OOOooO [ 8 : 10 ] :
       iiii11I = iiii11I - ( ( int ( O00OOOoOoo0O [ 8 : 10 ] ) - int ( ooo00OOOooO [ 8 : 10 ] ) ) * 40 )
      if iiii11I < 0 :
       iiii11I = 2400 + iiii11I
       iiii11I = iiii11I - ( 24 - int ( ooo00OOOooO [ 8 : 10 ] ) ) * 40
      return ( name , iI , o00O , OOO0OOO00oo , Iii111II , iiii11I , Ooo0OO0oOO , ii11i1 )
  except :
   pass
   if 1 - 1: I1i1iI1i / Oo0oO0ooo % i1iiIII111ii * iiIIi1IiIi11 . i11iIiiIii
def III1Iiii1I11 ( start_time , finish_time , recording_day , recording_month ) :
 oOO00oOO = ''
 IIII = True
 iiIiI = open ( iI1Ii11111iIi ) . read ( )
 o00oooO0Oo = re . findall ( '<programme>(.+?)</programme>' , iiIiI , re . DOTALL )
 for iiiIi1i1I in o00oooO0Oo :
  oOO00oOO = re . findall ( '<name>(.+?)</name>' , iiiIi1i1I ) [ 0 ]
  iI = re . findall ( '<hour_to_start>(.+?)</hour_to_start>' , iiiIi1i1I ) [ 0 ]
  o00O = re . findall ( '<minute_to_start>(.+?)</minute_to_start>' , iiiIi1i1I ) [ 0 ]
  OOO0OOO00oo = re . findall ( '<hour_to_end>(.+?)</hour_to_end>' , iiiIi1i1I ) [ 0 ]
  Iii111II = re . findall ( '<minute_to_end>(.+?)</minute_to_end>' , iiiIi1i1I ) [ 0 ]
  Ooo0OO0oOO = re . findall ( '<day>(.+?)</day>' , iiiIi1i1I ) [ 0 ]
  ii11i1 = re . findall ( '<month>(.+?)</month>' , iiiIi1i1I ) [ 0 ]
  if ii11i1 == recording_month and Ooo0OO0oOO == recording_day :
   o0O0OOO0Ooo = '%H:%M'
   iiIiII1 = start_time
   OOO00O0O = finish_time
   iii = iI + ':' + o00O
   oOooOOOoOo = OOO0OOO00oo + ':' + Iii111II
   if 41 - 41: oOOOO - O0 - O0
   if time . strptime ( iii , o0O0OOO0Ooo ) <= time . strptime ( iiIiII1 , o0O0OOO0Ooo ) <= time . strptime ( oOooOOOoOo , o0O0OOO0Ooo ) or time . strptime ( iii , o0O0OOO0Ooo ) <= time . strptime ( OOO00O0O , o0O0OOO0Ooo ) <= time . strptime ( oOooOOOoOo , o0O0OOO0Ooo ) or time . strptime ( iiIiII1 , o0O0OOO0Ooo ) <= time . strptime ( iii , o0O0OOO0Ooo ) <= time . strptime ( OOO00O0O , o0O0OOO0Ooo ) or time . strptime ( iiIiII1 , o0O0OOO0Ooo ) <= time . strptime ( oOooOOOoOo , o0O0OOO0Ooo ) <= time . strptime ( OOO00O0O , o0O0OOO0Ooo ) :
    if 68 - 68: i1iII1I1i1i1 % i1Ii
    if 88 - 88: iIii1I11I1II1 - ooOoo0O + i1iII1I1i1i1
    if 40 - 40: Oo0ooO0oo0oO * oOOOO + i1iII1I1i1i1 % i1iiIII111ii
    IIII = False
   else :
    pass
  else :
   pass
 return ( IIII , oOO00oOO )
 if 74 - 74: II1Iiii1111i - I1i1iI1i + OoooooooOO + i1Ii / o00
 if 23 - 23: O0
def o00oO0oOo00 ( name , url ) :
 name , iI , o00O , OOO0OOO00oo , Iii111II , iiii11I , Ooo0OO0oOO , ii11i1 = iiIii ( name )
 IiIIIi1iIi = iI + ':' + o00O ; ooOOoooooo = OOO0OOO00oo + ':' + Iii111II
 oO0oOo0 , I1I1I = III1Iiii1I11 ( IiIIIi1iIi , ooOOoooooo , Ooo0OO0oOO , ii11i1 )
 if oO0oOo0 == True :
  if not os . path . exists ( i1iII1IiiIiI1 ) :
   os . makedirs ( i1iII1IiiIiI1 )
  if not os . path . exists ( iI1Ii11111iIi ) :
   OoO0O00 = open ( iI1Ii11111iIi , "w+" )
  else :
   OoO0O00 = open ( iI1Ii11111iIi , "a+" )
  try :
   OoO0O00 . write ( '\n<programme>\n\t<name>' + name + '</name>\n\t<download_link>' + url + '</download_link>\n\t<hour_to_start>' + iI + '</hour_to_start>\n\t<minute_to_start>' + o00O + '</minute_to_start>\n\t<hour_to_end>' + OOO0OOO00oo + '</hour_to_end>\n\t<minute_to_end>' + Iii111II + '</minute_to_end>\n\t<duration>' + str ( iiii11I ) + '</duration>\n\t<day>' + Ooo0OO0oOO + '</day>\n\t<month>' + ii11i1 + '</month>\n</programme>' )
   iIiiiI . ok ( 'Recording ok' , 'Programme scheduled to record' )
  except :
   iIiiiI . ok ( 'Recording Error' , 'There was an error while trying to schedule recording' )
 else :
  iIiiiI . ok ( 'Recording Clash' , 'This recording clashes with "' + I1I1I + '"' , 'Please check "View recordings" to remove this' )
  if 95 - 95: o0OO0 + Oo0oO0ooo + i1iiIII111ii * iIii1I11I1II1 % II1Iiii1111i / iiIIi1IiIi11
  if 56 - 56: i1iiIII111ii
def oo0oO0oOOoo ( string ) :
 if len ( string ) == 1 :
  string = '0' + string
 return string
 if 51 - 51: I1i1iI1i * i11iIiiIii
def O0oo00o0O ( ) :
 i1I1I = time . gmtime ( )
 iiI1I = re . findall ( 'time.struct_time\(tm_year=(.+?), tm_mon=(.+?), tm_mday=(.+?), tm_hour=(.+?), tm_min=(.+?), .+?tm_isdst=(.+?)\)' , str ( i1I1I ) )
 for IiIiiIIiI , ooOO0OOOO0oo0 , I11iiI1i1 , I1i1Iiiii , OOo0oO00ooO00 , oOO0O00oO0Ooo in iiI1I :
  if oOO0O00oO0Ooo == '0' :
   I1i1Iiiii = int ( I1i1Iiiii ) + 1
  if int ( I1i1Iiiii ) >= 24 :
   I1i1Iiiii = int ( I1i1Iiiii ) - 24
  ooOO0OOOO0oo0 = oo0oO0oOOoo ( ooOO0OOOO0oo0 ) ; I11iiI1i1 = oo0oO0oOOoo ( I11iiI1i1 ) ; I1i1Iiiii = oo0oO0oOOoo ( str ( I1i1Iiiii ) ) ; OOo0oO00ooO00 = oo0oO0oOOoo ( OOo0oO00ooO00 )
 oO0Oo0O0o = IiIiiIIiI + ooOO0OOOO0oo0 + I11iiI1i1 + str ( I1i1Iiiii ) + OOo0oO00ooO00
 return oO0Oo0O0o
 if 99 - 99: II1Iiii1111i . i1iiIII111ii + ooOoo0O % II1Iiii1111i . i11iIiiIii % O0
 if 78 - 78: O0OOo + i1iII1I1i1i1 - i1Ii
def IIIIii1I ( ) :
 IiI1i = xbmcgui . Dialog ( ) . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11iiii1Ii = open ( I11i ) . read ( )
 II11iiii1Ii = II11iiii1Ii . replace ( '>USERNAME<' , I1IiI ) . replace ( '>PASSWORD<' , o0OOO )
 OO0o = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , II11iiii1Ii )
 for Ooo , O0o0Oo in OO0o :
  try :
   O0o0Oo = O0o0Oo . strip ( )
   Oo00OOOOO = re . findall ( 'name="(.+?)"' , Ooo ) [ 0 ]
   O0OO00o0OO = re . findall ( 'tvg-logo="(.+?)"' , Ooo ) [ 0 ]
   iI1iII1 = re . findall ( 'group-title="(.+?)"' , Ooo ) [ 0 ]
   if O0OO00o0OO [ 0 ] == '"' or 'base64' in O0OO00o0OO :
    O0OO00o0OO = Oo
   if IiI1i . lower ( ) . replace ( ' ' , '' ) in Oo00OOOOO . lower ( ) . replace ( ' ' , '' ) :
    iIi1ii1I1 ( Oo00OOOOO , O0o0Oo , 2 , O0OO00o0OO , '' , '' )
  except :
   pass
   if 92 - 92: iiIIi1IiIi11 . iiIIi1IiIi11 + o00ooo0
def IiIiI1111I1I ( name , url , icon , schedule = False ) :
 i1i = ''
 name = name . split ( ' -' ) [ 0 ]
 oOOoo00O00o = [ ]
 Iii1ii1II11i . create ( 'Beach Club Main' , 'Fetching EPG Data' )
 oO0Oo0O0o = O0oo00o0O ( )
 II11iiii1Ii = open ( I11i ) . read ( )
 II11iiii1Ii = II11iiii1Ii . replace ( '>USERNAME<' , I1IiI ) . replace ( '>PASSWORD<' , o0OOO )
 OO0o = re . findall ( '#EXTINF(.+?)\n' , II11iiii1Ii )
 for Ooo in OO0o :
  Oo00OOOOO = re . findall ( 'name="(.+?)"' , Ooo ) [ 0 ]
  if Oo00OOOOO == name :
   i1i = re . findall ( 'tvg-id="(.+?)"' , Ooo ) [ 0 ]
 if i1i != '' :
  ooo0O = oOoO0o00OO0 ( )
  Oo0oOOo = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , ooo0O , re . DOTALL )
  O0O00Oo = 0
  Iii1ii1II11i . update ( 0 , 'Creating EPG List' )
  for ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo in Oo0oOOo :
   ooOOO00Ooo = ooOOO00Ooo . replace ( '<' , '' ) . replace ( '&apos;' , '' ) . replace ( '\\/' , '/' )
   if i1i == O000OOo00oo :
    O0OoOoo00o = ooo00OOOooO [ 6 : 8 ] + '/' + ooo00OOOooO [ 4 : 6 ]
    IIIii1II1II = ooo00OOOooO [ 6 : 8 ] + '/' + ooo00OOOooO [ 4 : 6 ] + ' ' + ooo00OOOooO [ 8 : 10 ] + ':' + ooo00OOOooO [ 10 : 12 ]
    oooooo0O000o = time . strptime ( ooo00OOOooO [ 6 : 8 ] + '/' + ooo00OOOooO [ 4 : 6 ] , "%d/%m" )
    OoO = time . strptime ( oO0Oo0O0o [ 6 : 8 ] + '/' + oO0Oo0O0o [ 4 : 6 ] , "%d/%m" )
    if oooooo0O000o < OoO :
     pass
    else :
     oOOoo00O00o . append ( [ O000OOo00oo , oo0OOo , ooOOO00Ooo , IIIii1II1II , ooo00OOOooO [ 0 : 4 ] ] )
 if schedule == True :
  for ooO0O0O0ooOOO in oOOoo00O00o :
   Oo00OOOOO = ooO0O0O0ooOOO [ 3 ] + ' | ' + ooO0O0O0ooOOO [ 1 ] . replace ( '&apos;' , '' ) + '                                                                                                                            *' + ooO0O0O0ooOOO [ 3 ] + '*'
   try :
    IIIii1II1II = str ( ooO0O0O0ooOOO [ 3 ] )
    if time . gmtime ( ) < time . strptime ( ooO0O0O0ooOOO [ 4 ] + '/' + IIIii1II1II , '%Y/%d/%m %H:%M' ) :
     iIi1ii1I1 ( Oo00OOOOO . replace ( '&amp;' , '&' ) , url , 6 , icon , '' , ooO0O0O0ooOOO [ 2 ] )
   except :
    pass
 elif schedule == False :
  iIiiiI . textviewer (
 "EPG Data for " + name , '\n' . join ( IIIii1II1II + '\n' + oo0OOo + '\n' + ooOOO00Ooo + '\n\n' for O000OOo00oo , oo0OOo ,
 ooOOO00Ooo , IIIii1II1II , time_ in oOOoo00O00o if time . gmtime ( ) < time . strptime ( time_ + '/' + IIIii1II1II , '%Y/%d/%m %H:%M' ) ) )
  if 77 - 77: o00 - o0OO0 - ooOoo0O
def IiiiIIiIi1 ( Category ) :
 oOOoo00O00o = [ ]
 II11iiii1Ii = open ( I11i ) . read ( )
 II11iiii1Ii = II11iiii1Ii . replace ( '>USERNAME<' , I1IiI ) . replace ( '>PASSWORD<' , o0OOO )
 OO0o = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , II11iiii1Ii )
 if o0oOoO00o == 'true' :
  Iii1ii1II11i . create ( 'Beach Club Main' , 'Fetching EPG Data' )
  ooo0O = oOoO0o00OO0 ( )
  Oo0oOOo = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , ooo0O , re . DOTALL )
  O0O00Oo = 0
  Iii1ii1II11i . update ( 0 , 'Creating EPG List' )
  for ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo in Oo0oOOo :
   o0O0OOO0Ooo = '%d%m%Y %H:%M'
   ii11i1 = ooo00OOOooO [ 4 : 6 ] ; Ooo0OO0oOO = ooo00OOOooO [ 6 : 8 ] ; iI = ooo00OOOooO [ 8 : 10 ]
   o00O = ooo00OOOooO [ 10 : 12 ] ; OoOOoOooooOOo = ooo00OOOooO [ : 4 ]
   oOo0O = O00OOOoOoo0O [ 4 : 6 ] ; oo0O0 = O00OOOoOoo0O [ 6 : 8 ] ; iIOO0O000 = O00OOOoOoo0O [ 8 : 10 ]
   iiIiI1i1 = O00OOOoOoo0O [ 10 : 12 ] ; oO0O00oOOoooO = O00OOOoOoo0O [ : 4 ]
   IIIii1II1II = Ooo0OO0oOO + '/' + ii11i1 + ' ' + iI + ':' + o00O
   ooOOO00Ooo = ooOOO00Ooo . replace ( '<' , '' )
   oO0Oo0O0o = O0oo00o0O ( )
   IiIi11iI = oO0Oo0O0o [ 4 : 6 ] ; Oo0O00O000 = oO0Oo0O0o [ 6 : 8 ] ; i11I1IiII1i1i = oO0Oo0O0o [ 8 : 10 ]
   ooI1111i = oO0Oo0O0o [ 10 : 12 ] ; iIIii = oO0Oo0O0o [ : 4 ]
   IiIIIi1iIi = time . strptime ( Ooo0OO0oOO + ii11i1 + OoOOoOooooOOo + ' ' + iI + ':' + o00O , o0O0OOO0Ooo )
   i1I1I = time . strptime ( Oo0O00O000 + IiIi11iI + iIIii + ' ' + i11I1IiII1i1i + ':' + ooI1111i , o0O0OOO0Ooo )
   ooOOoooooo = time . strptime ( oo0O0 + oOo0O + oO0O00oOOoooO + ' ' + iIOO0O000 + ':' + iiIiI1i1 , o0O0OOO0Ooo )
   if 92 - 92: oOOOO + II1Iiii1111i % i1iII1I1i1i1
   if 62 - 62: O0OOo / i1IIi
   if IiIIIi1iIi <= i1I1I <= ooOOoooooo :
    oOOoo00O00o . append ( [ O000OOo00oo , oo0OOo , ooOOO00Ooo , IIIii1II1II ] )
    Iii1ii1II11i . update ( 0 , 'Created EPG List' )
 for Ooo , O0o0Oo in OO0o :
  O0o0Oo = O0o0Oo . strip ( )
  i1i = re . findall ( 'tvg-id="(.+?)"' , Ooo ) [ 0 ]
  Oo00OOOOO = re . findall ( 'name="(.+?)"' , Ooo ) [ 0 ]
  O0OO00o0OO = re . findall ( 'tvg-logo="(.+?)"' , Ooo ) [ 0 ]
  try :
   iI1iII1 = re . findall ( 'group-title="(.+?)"' , Ooo ) [ 0 ] . encode ( 'UTF-8' )
   oo0oO = Oo00OOOOO . encode ( 'UTF-8' )
   if o0oOoO00o == 'true' :
    O0O00Oo += 1
    if Iii1ii1II11i . iscanceled ( ) :
     return
    Iii1ii1II11i . update ( ( len ( OO0o ) / O0O00Oo ) * 100 , "Getting info for {}" . format ( Oo00OOOOO ) )
    for ooO0O0O0ooOOO in oOOoo00O00o :
     try :
      if i1i == ooO0O0O0ooOOO [ 0 ] :
       oo0oO = Oo00OOOOO + '\n' + ooO0O0O0ooOOO [ 1 ] + '\n' + ooO0O0O0ooOOO [ 2 ]
       oo0oO = oo0oO . replace ( '&apos;' , '' )
       Oo00OOOOO = Oo00OOOOO + ' - ' + ooO0O0O0ooOOO [ 1 ] . replace ( '&apos;' , '' ) + '                                                                                                                            *' + ooO0O0O0ooOOO [ 3 ] + '*'
     except :
      oo0oO = Oo00OOOOO
  except :
   pass
  if O0OO00o0OO [ 0 ] == '"' or 'base64' in O0OO00o0OO :
   O0OO00o0OO = Oo
  if Category == 'Full List' :
   try :
    try :
     iIi1ii1I1 ( Oo00OOOOO . encode ( 'UTF-8' ) , O0o0Oo , 2 , O0OO00o0OO , '' , oo0oO )
    except :
     iIi1ii1I1 ( Oo00OOOOO . encode ( 'UTF-8' ) , O0o0Oo , 2 , O0OO00o0OO , '' , '' )
   except :
    pass
  elif iI1iII1 == Category :
   try :
    try :
     iIi1ii1I1 ( Oo00OOOOO . encode ( 'UTF-8' ) , O0o0Oo , 2 , O0OO00o0OO , '' , oo0oO )
    except :
     iIi1ii1I1 ( Oo00OOOOO . encode ( 'UTF-8' ) , O0o0Oo , 2 , O0OO00o0OO , '' , '' )
   except :
    pass
    if 94 - 94: iIii1I11I1II1 / I1i1iI1i % i1iiIII111ii * i1iiIII111ii * o0OO0
def IIiIiI ( ) :
 if 94 - 94: II1Iiii1111i . i1IIi - Oo0oO0ooo % O0 - o00ooo0
 ooO0O00Oo0o = os . path . join ( i1iII1IiiIiI1 , 'm3ucache' , 'epg.txt' )
 OOO = ''
 oO0Oo0O0o = O0oo00o0O ( )
 I11iiI1i1 = oO0Oo0O0o [ 6 : 8 ] ; ooOO0OOOO0oo0 = oO0Oo0O0o [ 4 : 6 ]
 Oo0o00OO0000 = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' }
 I1i = requests . get ( o000o0o00o0Oo , headers = Oo0o00OO0000 ) . text
 Ooo = '<day>' + I11iiI1i1 + '</day><month>' + ooOO0OOOO0oo0 + '</month>\n'
 OOO += Ooo
 OOO += I1i
 OoO0O00 = open ( ooO0O00Oo0o , 'w+' )
 OoO0O00 . write ( OOO . encode ( 'UTF-8' ) )
 OoO0O00 . close ( )
 I1i = open ( ooO0O00Oo0o ) . read ( )
 return I1i
 if 99 - 99: i1Ii + o00 * iIii1I11I1II1 / OoooooooOO
def oOoO0o00OO0 ( ) :
 if 46 - 46: i1iIIII / oOOOO
 ooO0O00Oo0o = os . path . join ( i1iII1IiiIiI1 , 'm3ucache' , 'epg.txt' )
 oO0Oo0O0o = O0oo00o0O ( )
 I11iiI1i1 = oO0Oo0O0o [ 6 : 8 ] ; ooOO0OOOO0oo0 = oO0Oo0O0o [ 4 : 6 ]
 if not os . path . exists ( ooO0O00Oo0o ) :
  I1i = IIiIiI ( )
 else :
  O000 = open ( ooO0O00Oo0o ) . read ( )
  ooooooo00o , o0oooOO00 = re . findall ( '<day>(.+?)</day><month>(.+?)</month>' , str ( O000 ) ) [ 0 ]
  if ooooooo00o == I11iiI1i1 and o0oooOO00 == ooOO0OOOO0oo0 :
   I1i = open ( ooO0O00Oo0o ) . read ( )
  else :
   I1i = IIiIiI ( )
 return I1i
 if 32 - 32: i1Ii
def Iii1 ( ) :
 I1i = requests . get ( i1IIi11111i ) . content
 I1i = I1i . replace ( I1IiI , '>USERNAME<' ) . replace ( o0OOO , '>PASSWORD<' )
 oOOOoo00 = re . findall ( '(.+?)\n' , I1i . replace ( '*' , '' ) )
 if str ( I1i ) == '' :
  iiIiIIIiiI ( 'no data recieved' , 'Would you like to double check username and password in settings?' , '' , 'open_settings' )
 else :
  iiI1IIIi = open ( I11i , 'w+' )
  II11IiIi11 = open ( I11i , 'a' )
  II11IiIi11 . write ( '\n' . join ( str ( line ) for line in oOOOoo00 ) )
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 7 - 7: o00ooo0 . oOOOO % II1Iiii1111i * ooOoo0O + iiIIi1IiIi11 + i1Ii
def iiIiIIIiiI ( title , message1 , message2 , action ) :
 if iIiiiI . yesno ( title , message1 , message2 ) :
  if action == 'open_settings' :
   oo . openSettings ( sys . argv [ 0 ] )
   if 38 - 38: Oo0oO0ooo - Oo0ooO0oo0oO - Oo0oO0ooo / i1iIIII - i1IIi
def iIi1ii1I1 ( name , url , mode , iconimage , fanart , description , Folder = True ) :
 i1II1 = [ ]
 if mode == 2 : Folder = False
 elif mode == 6 : Folder = False
 elif mode == 16 : Folder = False
 elif mode == 1000 : Folder = False
 elif mode == 1001 : Folder = False
 if iconimage . startswith ( '.' ) :
  iconimage = iconimage [ 1 : ]
 if iconimage == '' or iconimage == '.' or iconimage == ' ' or 'goldtech.club' in iconimage :
  iconimage = Oo
 if fanart == '' : fanart = I1ii11iIi11i
 elif fanart == ' ' : fanart = I1ii11iIi11i
 i11i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name . encode ( 'UTF-8' ) ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus (
 description . encode ( 'UTF-8' ) )
 IiiiiI1i1Iii = True
 oo00oO0o = xbmcgui . ListItem ( name . encode ( 'UTF-8' ) , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name . encode ( 'UTF-8' ) , "Plot" : description . encode ( 'UTF-8' ) } )
 oo00oO0o . setProperty ( "Fanart_Image" , fanart )
 if o0oOoO00o == 'true' :
  if mode == 2 or mode == 6 :
   i1II1 . append ( ( 'Record' , 'XBMC.RunPlugin(%s?mode=6&name=%s&url=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) ) ) )
   i1II1 . append ( ( 'Create Series Link' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) ) ) )
  if mode == 2 :
   i1II1 . append ( ( 'View full epg listing' , 'XBMC.RunPlugin(%s?mode=5&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if mode == 16 :
   i1II1 . append ( ( 'Delete Recording' , 'XBMC.RunPlugin(%s?mode=13&name=%s&url=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) ) ) )
  if mode == 1000 :
   i1II1 . append ( ( 'Remove Series Link' , 'XBMC.RunPlugin(%s?mode=15&name=%s&url=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) ) ) )
  if mode == 1001 :
   i1II1 . append ( ( 'Cancel Recording' , 'XBMC.RunPlugin(%s?mode=17&name=%s&url=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) ) ) )
  oo00oO0o . addContextMenuItems ( i1II1 )
 IiiiiI1i1Iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11i1 , listitem = oo00oO0o , isFolder = Folder )
 return IiiiiI1i1Iii
 xbmc . executebuiltin ( 'Container.Refresh' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 31 - 31: i1iII1I1i1i1
def i1 ( name , url ) :
 xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name . encode ( 'UTF-8' ) ) )
 if 88 - 88: o00ooo0 - ooOoo0O + i1iII1I1i1i1 * Oo0ooO0oo0oO % iIii1I11I1II1 + I1i1iI1i
def oo000O0OoooO ( ) :
 O0o = [ ]
 I1i11II1i = sys . argv [ 2 ]
 if len ( I1i11II1i ) >= 2 :
  o0o0OoOo0O0OO = sys . argv [ 2 ]
  iIi1I11I = o0o0OoOo0O0OO . replace ( '?' , '' )
  if ( o0o0OoOo0O0OO [ len ( o0o0OoOo0O0OO ) - 1 ] == '/' ) :
   o0o0OoOo0O0OO = o0o0OoOo0O0OO [ 0 : len ( o0o0OoOo0O0OO ) - 2 ]
  Iii1ooO = iIi1I11I . split ( '&' )
  O0o = { }
  for OOoO000O0OO in range ( len ( Iii1ooO ) ) :
   o0o00OOo0 = { }
   o0o00OOo0 = Iii1ooO [ OOoO000O0OO ] . split ( '=' )
   if ( len ( o0o00OOo0 ) ) == 2 :
    O0o [ o0o00OOo0 [ 0 ] ] = o0o00OOo0 [ 1 ]
    if 17 - 17: i1Ii + II1Iiii1111i - i11iIiiIii . i1Ii * i1iII1I1i1i1
 return O0o
 if 77 - 77: i1IIi * i11iIiiIii % Oo0oO0ooo
o0o0OoOo0O0OO = oo000O0OoooO ( )
Oo0OoO00oOO0o = None
oOO00oOO = ''
IIIIiIiIi1 = None
I11iiiiI1i = None
iI1i11 = None
oo0oO = None
if 66 - 66: O0 % O0OOo + i11iIiiIii . o00 / oOOOO + O0OOo
try :
 Oo0OoO00oOO0o = urllib . unquote_plus ( o0o0OoOo0O0OO [ "url" ] )
except :
 pass
try :
 oOO00oOO = urllib . unquote_plus ( o0o0OoOo0O0OO [ "name" ] )
except :
 pass
try :
 IIIIiIiIi1 = urllib . unquote_plus ( o0o0OoOo0O0OO [ "iconimage" ] )
except :
 pass
try :
 I11iiiiI1i = int ( o0o0OoOo0O0OO [ "mode" ] )
except :
 pass
try :
 iI1i11 = urllib . unquote_plus ( o0o0OoOo0O0OO [ "fanart" ] )
except :
 pass
try :
 oo0oO = urllib . unquote_plus ( o0o0OoOo0O0OO [ "description" ] )
except :
 pass
 if 86 - 86: Oo0oO0ooo
if not os . path . exists ( I11i ) and I1IiI != '' and o0OOO != '' : Iii1 ( )
elif I1IiI == '' and o0OOO == '' : iiIiIIIiiI ( 'No username or password present' , 'Would you like to input username and password in settings?' , '' , 'open_settings' )
elif I11iiiiI1i == None : O0o0O00Oo0o0 ( )
elif I11iiiiI1i == 1 : IiiiIIiIi1 ( oOO00oOO )
elif I11iiiiI1i == 2 : i1 ( oOO00oOO , Oo0OoO00oOO0o )
elif I11iiiiI1i == 3 : Iii1 ( )
elif I11iiiiI1i == 4 : IIIIii1I ( )
elif I11iiiiI1i == 5 : IiIiI1111I1I ( oOO00oOO , Oo0OoO00oOO0o , Oo )
elif I11iiiiI1i == 6 : o00oO0oOo00 ( oOO00oOO , Oo0OoO00oOO0o )
elif I11iiiiI1i == 7 : o0O0o0Oo ( )
elif I11iiiiI1i == 8 : OooO0 ( oOO00oOO )
elif I11iiiiI1i == 9 : IiIiI1111I1I ( oOO00oOO , Oo0OoO00oOO0o , Oo , schedule = True )
elif I11iiiiI1i == 10 : o0oo0oOo ( oOO00oOO )
elif I11iiiiI1i == 11 : ooo ( )
elif I11iiiiI1i == 12 : O0o0 ( oOO00oOO , Oo0OoO00oOO0o )
elif I11iiiiI1i == 13 : I1 ( oOO00oOO )
elif I11iiiiI1i == 14 : ooOooo000oOO ( )
elif I11iiiiI1i == 15 : I111I11 ( oOO00oOO )
elif I11iiiiI1i == 16 : i1 ( oOO00oOO , Oo0OoO00oOO0o )
elif I11iiiiI1i == 17 : III1i1i ( oOO00oOO )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
