#!/usr/bin/python
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import xbmc , xbmcgui , xbmcplugin , xbmcaddon
import re , requests , os , sys , time , urllib2 , random
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'service.xbmc.beachclubmain'
oo = xbmcaddon . Addon ( id = o0OO00 )
i1iII1IiiIiI1 = xbmc . translatePath ( 'special://home/userdata/addon_data/' + str ( o0OO00 ) + '/' )
if 40 - 40: ooOoO0O00 * IIiIiII11i
o0oOOo0O0Ooo = xbmc . Monitor ( )
I1ii11iIi11i = xbmcgui . Dialog ( )
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
try :
 IiiIII111iI = 'plugin.video.beachclubmain'
 IiII = xbmcaddon . Addon ( id = IiiIII111iI )
 iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' + str ( IiiIII111iI ) + '/' )
 i1i1II = IiII . getSetting ( 'folder' )
 O0oo0OO0 = os . path . join ( i1iII1IiiIiI1 , 'awaiting_download.txt' )
 I1i1iiI1 = IiII . getSetting ( 'username' )
 iiIIIII1i1iI = IiII . getSetting ( 'password' )
 o0oO0 = IiII . getSetting ( 'delete' )
except :
 pass
oo00 = 'http://theonetv.vip/xmltv.php?username=' + I1i1iiI1 + '&password=' + iiIIIII1i1iI + '&type=m3u_plus&output=ts'
if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
if 1 - 1: O0Oooo00
if 87 - 87: i1IIi11111i / I11i1i11i1I % ooIiII1I1i1i1ii / oOOOo0o0O + OoOoo0 % O0Oooo00
def iIiiI1 ( ) :
 if 68 - 68: IIiIiII11i - i11iIiiIii - OOooOOo / i1iIii1Ii1II - OOooOOo + i1IIi
 IiiIII111ii = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' }
 if 3 - 3: I11i1i11i1I + O0
 I1Ii = requests . get ( oo00 , headers = IiiIII111ii ) . text
 return I1Ii
 if 66 - 66: i1IIi11111i
def oo0Ooo0 ( ) :
 if 46 - 46: OoOoo0 % OoOoo0 - II1iI * Ii1I % I11i1i11i1I
 OOooO0OOoo , iIii1 , oOOoO0 , O0OoO000O0OO , iiI1IiI = II ( )
 ooOoOoo0O = OOooO0OOoo + oOOoO0 + iIii1 + str ( O0OoO000O0OO ) + iiI1IiI
 if iiI1IiI > 10 :
  OooO0 = os . path . join ( i1iII1IiiIiI1 , 'series_link.txt' )
  if not os . path . exists ( i1iII1IiiIiI1 ) :
   os . makedirs ( i1iII1IiiIiI1 )
  if not os . path . exists ( OooO0 ) :
   open ( OooO0 , "w+" )
  II11iiii1Ii = open ( OooO0 ) . read ( )
  OO0o = iIiiI1 ( )
  Ooo = re . findall ( '<name>(.+?)</name><url>(.+?)</url>' , II11iiii1Ii )
  O0o0Oo = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , OO0o , re . DOTALL )
  for Oo00OOOOO , O0O in Ooo :
   try :
    O00o0OO , I11i1 , iIi1ii1I1 , o0 , I11II1i , IIIII , ooooooO0oo , IIiiiiiiIi1I1 = I1IIIii ( Oo00OOOOO )
    oOoOooOo0o0 = I11i1 + ':' + iIi1ii1I1 ; OOOO = o0 + ':' + I11II1i
    for OOO00 , iiiiiIIii , O000OO0 , I11iii1Ii , I1IIiiIiii in O0o0Oo :
     if not os . path . exists ( O0oo0OO0 ) :
      O000oo0O = open ( O0oo0OO0 , "w+" )
     else :
      O000oo0O = open ( O0oo0OO0 , "a+" )
     if O00o0OO in I11iii1Ii :
      OOOOi11i1 , IIIii1II1II = i1I1iI ( OOO00 [ 8 : 10 ] + ':' + OOO00 [ 10 : 12 ] , iiiiiIIii [ 8 : 10 ] + ':' + iiiiiIIii [ 10 : 12 ] , OOO00 [ 6 : 8 ] , OOO00 [ 4 : 6 ] )
      if OOOOi11i1 == True :
       oo0OooOOo0 = time . strptime ( OOO00 [ 6 : 8 ] + '/' + OOO00 [ 4 : 6 ] , "%d/%m" )
       o0O = time . strptime ( ooOoOoo0O [ 6 : 8 ] + '/' + ooOoOoo0O [ 4 : 6 ] , "%d/%m" )
       if oo0OooOOo0 < o0O :
        pass
       else :
        try :
         O000oo0O . write ( '\n<programme>\n\t<name>' + O00o0OO + '</name>\n\t<download_link>' + O0O + '</download_link>\n\t<hour_to_start>' + OOO00 [ 8 : 10 ] + '</hour_to_start>\n\t<minute_to_start>' + OOO00 [ 10 : 12 ] + '</minute_to_start>\n\t<hour_to_end>' + iiiiiIIii [ 8 : 10 ] + '</hour_to_end>\n\t<minute_to_end>' + iiiiiIIii [ 10 : 12 ] + '</minute_to_end>\n\t<duration>' + str ( IIIII ) + '</duration>\n\t<day>' + OOO00 [ 6 : 8 ] + '</day>\n\t<month>' + OOO00 [ 4 : 6 ] + '</month>\n</programme>' )
        except Exception as O00oO :
         xbmc . log ( 'Recording Error: There was an error while trying to schedule recording' , xbmc . LOGNOTICE )
         xbmc . log ( str ( O00oO ) , xbmc . LOGNOTICE )
   except :
    pass
    if 39 - 39: ooIiII1I1i1i1ii - ooOoO0O00 * OOooOOo % Ii1I * ooOoO0O00 % ooOoO0O00
    if 59 - 59: iIii1I11I1II1 + IIiIiII11i - Ii1I - IIiIiII11i + i1iIii1Ii1II / O0Oo0oO0o
    if 24 - 24: O0Oooo00 . I11i1i11i1I % i1iIii1Ii1II + OoOoo0 % I11i
def I1IIIii ( name ) :
 OO0o = iIiiI1 ( )
 if ':' in name :
  I11III1II , iI1I111Ii111i , I11IiI1I11i1i , iI1ii1Ii = re . findall ( '\*(.+?)/(.+?) (.+?):(.+?)\*' , name ) [ 0 ]
 try :
  name = name . split ( '- ' ) [ 1 ] . split ( ' *' ) [ 0 ]
 except :
  name = name . split ( '| ' ) [ 1 ] . split ( ' *' ) [ 0 ]
 while name [ - 1 ] == ' ' :
  name = name [ : - 1 ]
 O0o0Oo = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , OO0o , re . DOTALL )
 for OOO00 , iiiiiIIii , O000OO0 , I11iii1Ii , I1IIiiIiii in O0o0Oo :
  try :
   I1IIiiIiii = I1IIiiIiii . replace ( '<' , '' )
   if name . encode ( 'UTF-8' ) in I11iii1Ii . encode ( 'UTF-8' ) :
    IIiiiiiiIi1I1 = OOO00 [ 4 : 6 ] ; ooooooO0oo = OOO00 [ 6 : 8 ] ; I11i1 = OOO00 [ 8 : 10 ]
    iIi1ii1I1 = OOO00 [ 10 : 12 ] ; o0 = iiiiiIIii [ 8 : 10 ] ; I11II1i = iiiiiIIii [ 10 : 12 ] ; name = name
    if IIiiiiiiIi1I1 == iI1I111Ii111i and ooooooO0oo == I11III1II :
     if I11i1 == I11IiI1I11i1i and iIi1ii1I1 == iI1ii1Ii :
      oOoOooOo0o0 = int ( OOO00 [ 8 : 12 ] )
      OOOO = int ( iiiiiIIii [ 8 : 12 ] )
      IIIII = OOOO - oOoOooOo0o0
      if iiiiiIIii [ 8 : 10 ] > OOO00 [ 8 : 10 ] :
       IIIII = IIIII - ( ( int ( iiiiiIIii [ 8 : 10 ] ) - int ( OOO00 [ 8 : 10 ] ) ) * 40 )
      if IIIII < 0 :
       IIIII = 2400 + IIIII
       IIIII = IIIII - ( 24 - int ( OOO00 [ 8 : 10 ] ) ) * 40
      return ( name , I11i1 , iIi1ii1I1 , o0 , I11II1i , IIIII , ooooooO0oo , IIiiiiiiIi1I1 )
  except :
   pass
   if 92 - 92: I11i
def i1I1iI ( start_time , finish_time , recording_day , recording_month ) :
 O00o0OO = ''
 i1 = True
 OOO = open ( O0oo0OO0 ) . read ( )
 Oo0oOOo = re . findall ( '<programme>(.+?)</programme>' , OOO , re . DOTALL )
 for Oo0OoO00oOO0o in Oo0oOOo :
  O00o0OO = re . findall ( '<name>(.+?)</name>' , Oo0OoO00oOO0o ) [ 0 ]
  I11i1 = re . findall ( '<hour_to_start>(.+?)</hour_to_start>' , Oo0OoO00oOO0o ) [ 0 ]
  iIi1ii1I1 = re . findall ( '<minute_to_start>(.+?)</minute_to_start>' , Oo0OoO00oOO0o ) [ 0 ]
  o0 = re . findall ( '<hour_to_end>(.+?)</hour_to_end>' , Oo0OoO00oOO0o ) [ 0 ]
  I11II1i = re . findall ( '<minute_to_end>(.+?)</minute_to_end>' , Oo0OoO00oOO0o ) [ 0 ]
  ooooooO0oo = re . findall ( '<day>(.+?)</day>' , Oo0OoO00oOO0o ) [ 0 ]
  IIiiiiiiIi1I1 = re . findall ( '<month>(.+?)</month>' , Oo0OoO00oOO0o ) [ 0 ]
  if IIiiiiiiIi1I1 == recording_month and ooooooO0oo == recording_day :
   OOO00O = '%H:%M'
   OOoOO0oo0ooO = start_time
   O0o0O00Oo0o0 = finish_time
   O00O0oOO00O00 = I11i1 + ':' + iIi1ii1I1
   i1Oo00 = o0 + ':' + I11II1i
   if 31 - 31: oOOOo0o0O . I11i / O0
   if time . strptime ( O00O0oOO00O00 , OOO00O ) <= time . strptime ( OOoOO0oo0ooO , OOO00O ) <= time . strptime ( i1Oo00 , OOO00O ) or time . strptime ( O00O0oOO00O00 , OOO00O ) <= time . strptime ( O0o0O00Oo0o0 , OOO00O ) <= time . strptime ( i1Oo00 , OOO00O ) :
    if 89 - 89: I11i
    i1 = False
 return ( i1 , O00o0OO )
 if 68 - 68: OOooOOo * OoooooooOO % O0 + OOooOOo + OoOoo0
def i11i1I1 ( string ) :
 if len ( string ) == 1 :
  string = '0' + string
 return string
 if 36 - 36: iIii1I11I1II1 / I11i * i1iIii1Ii1II
def II ( ) :
 O0ii1ii1ii = time . gmtime ( )
 oooooOoo0ooo = re . findall ( 'time.struct_time\(tm_year=(.+?), tm_mon=(.+?), tm_mday=(.+?), tm_hour=(.+?), tm_min=(.+?), .+?tm_isdst=(.+?)\)' , str ( O0ii1ii1ii ) )
 for OOooO0OOoo , oOOoO0 , iIii1 , O0OoO000O0OO , iiI1IiI , I1I1IiI1 in oooooOoo0ooo :
  oOOoO0 = i11i1I1 ( oOOoO0 ) ; iIii1 = i11i1I1 ( iIii1 ) ; O0OoO000O0OO = i11i1I1 ( O0OoO000O0OO ) ; iiI1IiI = i11i1I1 ( iiI1IiI )
  if I1I1IiI1 == '0' :
   O0OoO000O0OO = int ( O0OoO000O0OO ) + 1
  return ( OOooO0OOoo , iIii1 , oOOoO0 , O0OoO000O0OO , iiI1IiI )
  if 5 - 5: Ii1I * OoOoo0 + I11i . i1iIii1Ii1II + I11i
  if 91 - 91: O0
def oOOo0 ( ) :
 while True :
  if o0oOOo0O0Ooo . waitForAbort ( 4 ) :
   sys . exit ( 0 )
  else :
   oo00O00oO ( )
   oo0Ooo0 ( )
   if 23 - 23: OOooOOo + OOooOOo . i1iIii1Ii1II
def ii1ii11IIIiiI ( ) :
 import datetime as DT
 O00OOOoOoo0O = DT . date . today ( )
 O000OOo00oo = O00OOOoOoo0O - DT . timedelta ( days = o0oO0 )
 for oo0OOo in os . walk ( i1i1II ) . next ( ) [ 2 ] :
  if '.mp4' in oo0OOo :
   ooOOO00Ooo = oo0OOo . replace ( '.mp4' , '' )
   iIii1 = ooOOO00Ooo [ - 4 : - 2 ] ; oOOoO0 = ooOOO00Ooo [ - 2 : ]
   iIii1 = DT . datetime . strptime ( iIii1 + oOOoO0 + '2018' , "%d%m%Y" ) . date ( )
   if iIii1 < O000OOo00oo :
    IiIIIi1iIi = os . path . join ( i1i1II , oo0OOo )
    os . remove ( IiIIIi1iIi )
    if 68 - 68: i11iIiiIii % O0Oo0oO0o + i11iIiiIii
def iii ( ) :
 ii1ii11IIIiiI ( )
 II1I = [ ]
 O0i1II1Iiii1I11 = [ ]
 IIII = ''
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - Ii1I
 O0oo0OO0 = os . path . join ( i1iII1IiiIiI1 , 'awaiting_download.txt' )
 OOooO0OOoo , O00OOOoOoo0O , oOOoO0 , O0OoO000O0OO , iiI1IiI = II ( )
 if 91 - 91: I11i1i11i1I % i1IIi % iIii1I11I1II1
 with open ( O0oo0OO0 ) as IIi1I11I1II :
  for OooOoooOo , ii11IIII11I in enumerate ( IIi1I11I1II ) :
   if '<month>' in ii11IIII11I :
    OOooo = re . findall ( '<month>(.+?)</month>' , ii11IIII11I ) [ 0 ]
    oOooOOOoOo = OooOoooOo - 1
    O0i1II1Iiii1I11 . append ( [ OOooo , oOooOOOoOo ] )
  IIi1I11I1II . close ( )
 with open ( O0oo0OO0 ) as IIi1I11I1II :
  for OooOoooOo , ii11IIII11I in enumerate ( IIi1I11I1II ) :
   for OOooo , oOooOOOoOo in O0i1II1Iiii1I11 :
    if OooOoooOo == oOooOOOoOo :
     iIii1 = re . findall ( '<day>(.+?)</day>' , ii11IIII11I ) [ 0 ]
     oo0OooOOo0 = time . strptime ( iIii1 + '/' + OOooo , "%d/%m" )
     o0O = time . strptime ( O00OOOoOoo0O + '/' + oOOoO0 , "%d/%m" )
     if oo0OooOOo0 < o0O :
      II1I . append ( [ OooOoooOo - 8 , OooOoooOo + 3 ] )
  IIi1I11I1II . close ( )
 with open ( O0oo0OO0 ) as IIi1I11I1II :
  for i1Iii1i1I in II1I :
   for OooOoooOo , ii11IIII11I in enumerate ( IIi1I11I1II ) :
    if OooOoooOo in range ( i1Iii1i1I [ 0 ] , i1Iii1i1I [ 1 ] ) :
     pass
    else :
     IIII += ii11IIII11I
  IIi1I11I1II . close ( )
 if IIII != '' :
  OOoO00 = open ( O0oo0OO0 , 'w+' )
  OOoO00 . write ( IIII )
  OOoO00 . close ( )
  if 40 - 40: IIiIiII11i * i1IIi11111i + i1iIii1Ii1II % I11i1i11i1I
def oo00O00oO ( ) :
 O0oo0OO0 = os . path . join ( i1iII1IiiIiI1 , 'awaiting_download.txt' )
 if not os . path . exists ( i1iII1IiiIiI1 ) :
  os . makedirs ( i1iII1IiiIiI1 )
 if not os . path . exists ( O0oo0OO0 ) :
  open ( O0oo0OO0 , "w+" )
 II11iiii1Ii = open ( O0oo0OO0 ) . read ( )
 if II11iiii1Ii != '' :
  OOooO0OOoo , iIii1 , oOOoO0 , O0OoO000O0OO , iiI1IiI = II ( )
  try :
   iii ( )
  except :
   pass
  try :
   OOOOOoo0 = re . findall ( '<programme>(.+?)</programme>' , str ( II11iiii1Ii ) , re . DOTALL )
   for Oo0OoO00oOO0o in OOOOOoo0 :
    O00o0OO = re . findall ( '<name>(.+?)</name>' , Oo0OoO00oOO0o ) [ 0 ]
    ii1 = re . findall ( '<download_link>(.+?)</download_link>' , Oo0OoO00oOO0o ) [ 0 ]
    I11i1 = re . findall ( '<hour_to_start>(.+?)</hour_to_start>' , Oo0OoO00oOO0o ) [ 0 ]
    iIi1ii1I1 = re . findall ( '<minute_to_start>(.+?)</minute_to_start>' , Oo0OoO00oOO0o ) [ 0 ]
    o0 = re . findall ( '<hour_to_end>(.+?)</hour_to_end>' , Oo0OoO00oOO0o ) [ 0 ]
    I11II1i = re . findall ( '<minute_to_end>(.+?)</minute_to_end>' , Oo0OoO00oOO0o ) [ 0 ]
    IIIII = re . findall ( '<duration>(.+?)</duration>' , Oo0OoO00oOO0o ) [ 0 ]
    ooooooO0oo = re . findall ( '<day>(.+?)</day>' , Oo0OoO00oOO0o ) [ 0 ]
    IIiiiiiiIi1I1 = re . findall ( '<month>(.+?)</month>' , Oo0OoO00oOO0o ) [ 0 ]
    if IIiiiiiiIi1I1 == oOOoO0 and ooooooO0oo == iIii1 :
     I1iI1iIi111i = int ( I11i1 ) - int ( O0OoO000O0OO )
     if I1iI1iIi111i <= 1 :
      print IIIII
      iiIi1IIi1I = int ( I11i1 + iIi1ii1I1 )
      o0OoOO000ooO0 = int ( str ( O0OoO000O0OO ) + str ( iiI1IiI ) )
      o0o0o0oO0oOO = int ( str ( I11i1 ) + str ( iIi1ii1I1 ) )
      ii1Ii11I = int ( str ( o0 ) + str ( I11II1i ) )
      if ii1Ii11I < o0OoOO000ooO0 :
       continue
      if o0o0o0oO0oOO <= o0OoOO000ooO0 <= ii1Ii11I :
       IIIII = ii1Ii11I - o0OoOO000ooO0
       if int ( o0 ) > int ( O0OoO000O0OO ) :
        o00o0 = int ( o0 ) - int ( O0OoO000O0OO )
        IIIII = int ( IIIII ) - ( 40 * int ( o00o0 ) )
      ii = int ( iiIi1IIi1I ) - int ( o0OoOO000ooO0 )
      if I11i1 > O0OoO000O0OO :
       ii = ii - 40
      print ii
      if ii <= 2 :
       OOooooO0Oo ( O00o0OO , ii1 , IIIII )
  except Exception as O00oO :
   xbmc . log ( str ( O00oO ) , xbmc . LOGNOTICE )
   if 91 - 91: Ii1I . iIii1I11I1II1 / II1iI + i1IIi
   if 42 - 42: OoOoo0 . Ii1I . OoOoo0 - O0Oo0oO0o
def OOooooO0Oo ( name , download_link , duration ) :
 i1ii1I1I1 = 501
 try :
  name = name . split ( '| ' ) [ 1 ]
 except :
  name = name
 OOooO0OOoo , O00OOOoOoo0O , oOOoO0 , O0OoO000O0OO , iiI1IiI = II ( )
 duration = int ( duration ) + 2
 name = name . replace ( '*' , '' ) . replace ( ':' , '' )
 oOoOooOo0o0 = time . time ( )
 oO = urllib2 . build_opener ( )
 oO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' ) ]
 II11iiii1Ii = oO . open ( download_link )
 oO0O0o0Oooo = os . path . join ( i1i1II , name + ' ' + str ( O0OoO000O0OO ) + str ( iiI1IiI ) + str ( O00OOOoOoo0O ) + str ( oOOoO0 ) + '.mp4' )
 I1Ii1iI1 = open ( oO0O0o0Oooo , 'wb' )
 oO0 = 512
 while True :
  try :
   try :
    O0OO0O = xbmc . getInfoLabel ( 'System.FreeSpace' )
    i1ii1I1I1 = int ( O0OO0O . replace ( ' MB' , '' ) . replace ( ' Free' , '' ) )
   except :
    pass
   if i1ii1I1I1 > 500 :
    OO = II11iiii1Ii . read ( oO0 )
    if not OO :
     break
    OoOoO = time . time ( )
    Ii1I1i = OoOoO - oOoOooOo0o0
    if OoOoO >= oOoOooOo0o0 + 60 * int ( duration ) :
     break
    I1Ii1iI1 . write ( OO )
    if 99 - 99: II1iI . I11i1i11i1I + OoOoo0 % II1iI . i11iIiiIii % O0
  except Exception , O00oO :
   xbmc . log ( str ( O00oO ) , xbmc . LOGNOTICE )
 I1Ii1iI1 . close ( )
 if 78 - 78: O0Oo0oO0o + i1iIii1Ii1II - oOOOo0o0O
try :
 oOOo0 ( )
except :
 pass # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
