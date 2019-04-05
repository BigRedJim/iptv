#!/usr/bin/env python
# -*-mode: python; coding: utf-8 -*-
import sys
import xbmcplugin
import xbmcgui
import xbmc
import xbmcaddon
import requests
import re
import os
import urllib
import time
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.higgytv'
Oo0Ooo = xbmcaddon . Addon ( id = OO0o )
O0O0OO0O0O0 = xbmc . translatePath ( 'special://home/addons/' + str ( OO0o ) + '/' )
iiiii = os . path . join ( O0O0OO0O0O0 , 'm3ucache' , 'temp.m3u' )
ooo0OO = os . path . join ( O0O0OO0O0O0 , 'm3ucache' )
if not os . path . exists ( ooo0OO ) :
 os . makedirs ( ooo0OO )
II1 = os . path . join ( O0O0OO0O0O0 , 'm3ucache' , 'logo.txt' )
O00ooooo00 = os . path . join ( O0O0OO0O0O0 , 'icon.png' )
I1IiiI = os . path . join ( O0O0OO0O0O0 , 'fanart.jpg' )
IIi1IiiiI1Ii = Oo0Ooo . getSetting ( 'username' )
I11i11Ii = Oo0Ooo . getSetting ( 'password' )
oO00oOo = xbmcgui . Dialog ( )
OOOo0 = xbmcgui . DialogProgress ( )
if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
o0O = Oo0Ooo . getSetting ( "epg" )
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = 'http://176.9.140.236:25461/get.php?username=' + IIi1IiiiI1Ii + '&password=' + I11i11Ii + '&type=m3u_plus&output=ts'
i1ii1iIII = 'http://176.9.140.236:25461/xmltv.php?username=' + IIi1IiiiI1Ii + '&password=' + I11i11Ii + '&type=m3u_plus&output=ts'
if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
if 56 - 56: ooO00oOoo - O0OOo
def II1Iiii1111i ( string ) :
 if len ( string ) == 1 :
  string = '0' + string
 return string
 if 25 - 25: OOo000
def O0 ( ) :
 I11i1i11i1I = time . gmtime ( )
 Iiii = re . findall ( 'time.struct_time\(tm_year=(.+?), tm_mon=(.+?), tm_mday=(.+?), tm_hour=(.+?), tm_min=(.+?), .+?tm_isdst=(.+?)\)' , str ( I11i1i11i1I ) )
 for OOO0O , oo0ooO0oOOOOo , oO000OoOoo00o , iiiI11 , OOooO , OOoO00o in Iiii :
  oo0ooO0oOOOOo = II1Iiii1111i ( oo0ooO0oOOOOo ) ; oO000OoOoo00o = II1Iiii1111i ( oO000OoOoo00o ) ; iiiI11 = II1Iiii1111i ( iiiI11 ) ; OOooO = II1Iiii1111i ( OOooO )
  if OOoO00o == '0' :
   iiiI11 = int ( iiiI11 ) + 1
 II111iiii = OOO0O + oo0ooO0oOOOOo + oO000OoOoo00o + str ( iiiI11 ) + OOooO
 return II111iiii
 if 48 - 48: I1Ii . IiIi1Iii1I1 - IiIi1Iii1I1 % IiIi1Iii1I1 - o00ooo0 * Oo0oO0ooo
def O00OooO0 ( name , url , icon , schedule = False ) :
 Ooooo = ''
 name = name . split ( ' -' ) [ 0 ]
 o00o = [ ]
 OOOo0 . create ( 'Higgy TV' , 'Fetching EPG Data' )
 II111iiii = O0 ( )
 IiI1I1 = open ( iiiii ) . read ( )
 IiI1I1 = IiI1I1 . replace ( '>USERNAME<' , IIi1IiiiI1Ii ) . replace ( '>PASSWORD<' , I11i11Ii )
 OoO000 = re . findall ( '#EXTINF(.+?)\n' , IiI1I1 )
 for IIiiIiI1 in OoO000 :
  iiIiIIi = re . findall ( 'name="(.+?)"' , IIiiIiI1 ) [ 0 ]
  if iiIiIIi == name :
   Ooooo = re . findall ( 'tvg-id="(.+?)"' , IIiiIiI1 ) [ 0 ]
 if Ooooo != '' :
  ooOoo0O = OooO0 ( )
  II11iiii1Ii = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)/desc>' , ooOoo0O , re . DOTALL )
  OO0oOoo = 0
  OOOo0 . update ( 0 , 'Creating EPG List' )
  for O0o0Oo , Oo00OOOOO , O0O , O00o0OO , I11i1 in II11iiii1Ii :
   I11i1 = I11i1 . replace ( '<' , '' ) . replace ( '&apos;' , '' ) . replace ( '\\/' , '/' )
   if Ooooo == O0O :
    iIi1ii1I1 = O0o0Oo [ 6 : 8 ] + '/' + O0o0Oo [ 4 : 6 ]
    o0I11II1i = O0o0Oo [ 6 : 8 ] + '/' + O0o0Oo [ 4 : 6 ] + ' ' + O0o0Oo [ 8 : 10 ] + ':' + O0o0Oo [ 10 : 12 ]
    IIIII = time . strptime ( O0o0Oo [ 6 : 8 ] + '/' + O0o0Oo [ 4 : 6 ] , "%d/%m" )
    ooooooO0oo = time . strptime ( II111iiii [ 6 : 8 ] + '/' + II111iiii [ 4 : 6 ] , "%d/%m" )
    if IIIII < ooooooO0oo :
     pass
    else :
     o00o . append ( [ O0O , O00o0OO , I11i1 , o0I11II1i , O0o0Oo [ 0 : 4 ] ] )
 if schedule == True :
  for IIiiiiiiIi1I1 in o00o :
   iiIiIIi = IIiiiiiiIi1I1 [ 3 ] + ' | ' + IIiiiiiiIi1I1 [ 1 ] . replace ( '&apos;' , '' ) + '                                                                                                                            *' + IIiiiiiiIi1I1 [ 3 ] + '*'
   try :
    o0I11II1i = str ( IIiiiiiiIi1I1 [ 3 ] )
    if time . gmtime ( ) < time . strptime ( IIiiiiiiIi1I1 [ 4 ] + '/' + o0I11II1i , '%Y/%d/%m %H:%M' ) :
     I1IIIii ( iiIiIIi . replace ( '&amp;' , '&' ) , url , 6 , icon , '' , IIiiiiiiIi1I1 [ 2 ] )
   except :
    pass
 elif schedule == False :
  oO00oOo . textviewer (
 "EPG Data for " + name , '\n' . join ( o0I11II1i + '\n' + O00o0OO + '\n' + I11i1 + '\n\n' for O0O , O00o0OO ,
 I11i1 , o0I11II1i , time_ in o00o if time . gmtime ( ) < time . strptime ( time_ + '/' + o0I11II1i , '%Y/%d/%m %H:%M' ) ) )
  if 95 - 95: I1Ii111 % o00ooo0 . i1
def I1i1I ( ) :
 oOO00oOO = [ ]
 I1IIIii ( 'Update Channel List' , '' , 3 , '' , '' , '' )
 I1IIIii ( 'Search Channel' , '' , 4 , '' , '' , '' )
 I1IIIii ( 'Full List' , '' , 1 , '' , '' , '' )
 IiI1I1 = open ( iiiii ) . read ( )
 IiI1I1 = IiI1I1 . replace ( '>USERNAME<' , IIi1IiiiI1Ii ) . replace ( '>PASSWORD<' , I11i11Ii )
 OoO000 = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , IiI1I1 )
 for IIiiIiI1 , OoOo in OoO000 :
  try :
   iI = re . findall ( 'group-title="(.+?)"' , IIiiIiI1 ) [ 0 ]
   if iI not in str ( oOO00oOO ) :
    oOO00oOO . append ( iI )
  except :
   pass
 for o00O in oOO00oOO :
  try :
   I1IIIii ( o00O , '' , 1 , '' , '' , '' )
  except :
   pass
   if 69 - 69: o00ooo0 % I1Ii - o00O0oo + I1Ii - i1 % i1oOo0OoO
def Iii111II ( ) :
 iiii11I = xbmcgui . Dialog ( ) . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiI1I1 = open ( iiiii ) . read ( )
 IiI1I1 = IiI1I1 . replace ( '>USERNAME<' , IIi1IiiiI1Ii ) . replace ( '>PASSWORD<' , I11i11Ii )
 OoO000 = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , IiI1I1 )
 for IIiiIiI1 , OoOo in OoO000 :
  OoOo = OoOo . strip ( )
  iiIiIIi = re . findall ( 'name="(.+?)"' , IIiiIiI1 ) [ 0 ]
  Ooo0OO0oOO = re . findall ( 'tvg-logo="(.+?)"' , IIiiIiI1 ) [ 0 ]
  iI = re . findall ( 'group-title="(.+?)"' , IIiiIiI1 ) [ 0 ]
  if Ooo0OO0oOO [ 0 ] == '"' or 'base64' in Ooo0OO0oOO :
   Ooo0OO0oOO = O00ooooo00
  if iiii11I . lower ( ) . replace ( ' ' , '' ) in iiIiIIi . lower ( ) . replace ( ' ' , '' ) :
   I1IIIii ( iiIiIIi , OoOo , 2 , Ooo0OO0oOO , '' , '' )
   if 50 - 50: iII111i
def Ii1i11IIii1I ( Category ) :
 o00o = [ ]
 IiI1I1 = open ( iiiii ) . read ( )
 IiI1I1 = IiI1I1 . replace ( '>USERNAME<' , IIi1IiiiI1Ii ) . replace ( '>PASSWORD<' , I11i11Ii )
 OoO000 = re . findall ( '#EXTINF(.+?)\n(.+?)\n' , IiI1I1 )
 if o0O == 'true' :
  OOOo0 . create ( 'Higgy TV' , 'Fetching EPG Data' )
  ooOoo0O = OooO0 ( )
  II11iiii1Ii = re . findall ( 'start="(.+?)" stop="(.+?)" channel="(.+?)".+?><title>(.+?)</title><desc>(.+?)</desc>' , ooOoo0O , re . DOTALL )
  OO0oOoo = 0
  OOOo0 . update ( 0 , 'Creating EPG List' )
  for O0o0Oo , Oo00OOOOO , O0O , O00o0OO , I11i1 in II11iiii1Ii :
   II111iiii = O0 ( )
   OOOoO0O0o = O0o0Oo . replace ( '+0100' , '' ) . replace ( ' ' , '' ) [ : 12 ]
   O0o0Ooo = Oo00OOOOO . replace ( '+0100' , '' ) . replace ( ' ' , '' ) [ : 12 ]
   if OOOoO0O0o < II111iiii < O0o0Ooo :
    o00o . append ( [ O0O , O00o0OO , I11i1 ] )
    OOOo0 . update ( 0 , 'Created EPG List' )
 for IIiiIiI1 , OoOo in OoO000 :
  OoOo = OoOo . strip ( )
  Ooooo = re . findall ( 'tvg-id="(.+?)"' , IIiiIiI1 ) [ 0 ]
  iiIiIIi = re . findall ( 'name="(.+?)"' , IIiiIiI1 ) [ 0 ]
  Ooo0OO0oOO = re . findall ( 'tvg-logo="(.+?)"' , IIiiIiI1 ) [ 0 ]
  try :
   iI = re . findall ( 'group-title="(.+?)"' , IIiiIiI1 ) [ 0 ]
   O00 = iiIiIIi
   if o0O == 'true' :
    OO0oOoo += 1
    if OOOo0 . iscanceled ( ) :
     return
    OOOo0 . update ( ( len ( OoO000 ) / OO0oOoo ) * 100 , "Getting info for {}" . format ( iiIiIIi ) )
    for IIiiiiiiIi1I1 in o00o :
     if 47 - 47: O0OOo
     if Ooooo == IIiiiiiiIi1I1 [ 0 ] :
      O00 = iiIiIIi + '\n' + IIiiiiiiIi1I1 [ 1 ] + '\n' + IIiiiiiiIi1I1 [ 2 ]
      O00 = O00 . replace ( '&apos;' , '' )
      iiIiIIi = iiIiIIi + ' - ' + IIiiiiiiIi1I1 [ 1 ] . replace ( '&apos;' , '' )
      if 50 - 50: Oo - IiIi1Iii1I1 * II1i / I1Ii + o00O0oo
      if 88 - 88: ooO00oOoo / I1Ii + O0OOo - Oo / IiIi1Iii1I1 - ooOoO0o
  except :
   pass
  if Ooo0OO0oOO [ 0 ] == '"' or 'base64' in Ooo0OO0oOO :
   Ooo0OO0oOO = O00ooooo00
  if Category == 'Full_List' :
   try :
    I1IIIii ( iiIiIIi , OoOo , 2 , Ooo0OO0oOO , '' , O00 )
   except :
    pass
  elif iI == Category :
   try :
    I1IIIii ( iiIiIIi , OoOo , 2 , Ooo0OO0oOO , '' , O00 )
   except :
    pass
    if 15 - 15: II1i + ooOoO0o - i1oOo0OoO / o00
def oo000OO00Oo ( ) :
 if 51 - 51: OOo000 * o00O0oo + Oo0oO0ooo + I1Ii111
 o0O0O00 = os . path . join ( O0O0OO0O0O0 , 'm3ucache' , 'epg.txt' )
 o000o = ''
 II111iiii = O0 ( )
 oO000OoOoo00o = II111iiii [ 6 : 8 ] ; oo0ooO0oOOOOo = II111iiii [ 4 : 6 ]
 I11IiI1I11i1i = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' }
 iI1ii1Ii = requests . get ( i1ii1iIII , headers = I11IiI1I11i1i ) . text
 IIiiIiI1 = '<day>' + oO000OoOoo00o + '</day><month>' + oo0ooO0oOOOOo + '</month>\n'
 o000o += IIiiIiI1
 o000o += iI1ii1Ii
 oooo000 = open ( o0O0O00 , 'w+' )
 oooo000 . write ( o000o . encode ( 'UTF-8' ) )
 oooo000 . close ( )
 iI1ii1Ii = open ( o0O0O00 ) . read ( )
 return iI1ii1Ii
 if 16 - 16: II1i + I1Ii111 - Oo
def OooO0 ( ) :
 if 85 - 85: ooOoO0o + iIIIiiIIiiiIi
 o0O0O00 = os . path . join ( O0O0OO0O0O0 , 'm3ucache' , 'epg.txt' )
 II111iiii = O0 ( )
 oO000OoOoo00o = II111iiii [ 6 : 8 ] ; oo0ooO0oOOOOo = II111iiii [ 4 : 6 ]
 if not os . path . exists ( o0O0O00 ) :
  iI1ii1Ii = oo000OO00Oo ( )
 else :
  Oo0OoO00oOO0o = open ( o0O0O00 ) . read ( )
  OOO00O , OOoOO0oo0ooO = re . findall ( '<day>(.+?)</day><month>(.+?)</month>' , str ( Oo0OoO00oOO0o ) ) [ 0 ]
  if OOO00O == oO000OoOoo00o and OOoOO0oo0ooO == oo0ooO0oOOOOo :
   iI1ii1Ii = open ( o0O0O00 ) . read ( )
  else :
   iI1ii1Ii = oo000OO00Oo ( )
 return iI1ii1Ii
def O0o0O00Oo0o0 ( ) :
 iI1ii1Ii = requests . get ( O0oOO0o0 ) . content
 iI1ii1Ii = iI1ii1Ii . replace ( IIi1IiiiI1Ii , '>USERNAME<' ) . replace ( I11i11Ii , '>PASSWORD<' )
 O00O0oOO00O00 = re . findall ( '(.+?)\n' , iI1ii1Ii )
 if str ( iI1ii1Ii ) == '' :
  i1Oo00 ( 'no data recieved' , 'Would you like to double check username and password in settings?' , '' , 'open_settings' )
 else :
  i1i = open ( iiiii , 'w+' )
  iiI111I1iIiI = open ( iiiii , 'a' )
  iiI111I1iIiI . write ( '\n' . join ( str ( line ) for line in O00O0oOO00O00 ) )
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 41 - 41: IiII . IiIi1Iii1I1 + i1 * o00O0oo % IiII * IiII
def i1Oo00 ( title , message1 , message2 , action ) :
 if oO00oOo . yesno ( title , message1 , message2 ) :
  if action == 'open_settings' :
   Oo0Ooo . openSettings ( sys . argv [ 0 ] )
   if 19 - 19: O0OOo
def I1IIIii ( name , url , mode , iconimage , fanart , description , Folder = True ) :
 IIi1iiIi1 = [ ]
 if mode == 2 : Folder = False
 if mode == 3 : Folder = False
 if iconimage == '' : iconimage = O00ooooo00
 elif iconimage == ' ' : iconimage = O00ooooo00
 if fanart == '' : fanart = I1IiiI
 elif fanart == ' ' : fanart = I1IiiI
 iii1i1iiiiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiiOO0OoO0o00 = True
 ooOO0O0ooOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO0O0ooOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO0O0ooOooO . setProperty ( "Fanart_Image" , fanart )
 if mode == 2 :
  IIi1iiIi1 . append ( ( 'View 24hrs EPG listing' , 'XBMC.RunPlugin(%s?mode=5&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  ooOO0O0ooOooO . addContextMenuItems ( IIi1iiIi1 )
 IiiiOO0OoO0o00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1i1iiiiIi , listitem = ooOO0O0ooOooO , isFolder = Folder )
 return IiiiOO0OoO0o00
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 55 - 55: o00O0oo * ooOoO0o
def o0O00oOoOO ( name , url ) :
 xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 if 42 - 42: I1Ii111
def o0o ( ) :
 o00OooOO000 = [ ]
 OOoOoo = sys . argv [ 2 ]
 if len ( OOoOoo ) >= 2 :
  oO0000OOo00 = sys . argv [ 2 ]
  iiIi1IIiIi = oO0000OOo00 . replace ( '?' , '' )
  if ( oO0000OOo00 [ len ( oO0000OOo00 ) - 1 ] == '/' ) :
   oO0000OOo00 = oO0000OOo00 [ 0 : len ( oO0000OOo00 ) - 2 ]
  oOO00Oo = iiIi1IIiIi . split ( '&' )
  o00OooOO000 = { }
  for i1iIIIi1i in range ( len ( oOO00Oo ) ) :
   iI1iIIiiii = { }
   iI1iIIiiii = oOO00Oo [ i1iIIIi1i ] . split ( '=' )
   if ( len ( iI1iIIiiii ) ) == 2 :
    o00OooOO000 [ iI1iIIiiii [ 0 ] ] = iI1iIIiiii [ 1 ]
    if 26 - 26: Oo0oO0ooo . i1oOo0OoO
 return o00OooOO000
 if 39 - 39: O0OOo - i1 % i11iIiiIii * I1Ii . OOo000
oO0000OOo00 = o0o ( )
OOooo0O00o = None
oOOoOooOo = ''
O000oo = None
IIi1I11I1II = None
OooOoooOo = None
if 46 - 46: O0OOo
try :
 OOooo0O00o = urllib . unquote_plus ( oO0000OOo00 [ "url" ] )
except :
 pass
try :
 oOOoOooOo = urllib . unquote_plus ( oO0000OOo00 [ "name" ] )
except :
 pass
try :
 O000oo = urllib . unquote_plus ( oO0000OOo00 [ "iconimage" ] )
except :
 pass
try :
 IIi1I11I1II = int ( oO0000OOo00 [ "mode" ] )
except :
 pass
try :
 OooOoooOo = urllib . unquote_plus ( oO0000OOo00 [ "fanart" ] )
except :
 pass
try :
 O00 = urllib . unquote_plus ( oO0000OOo00 [ "description" ] )
except :
 pass
 if 8 - 8: o00ooo0 * ooOoO0o - ooO00oOoo - I1Ii111 * o00 % iII111i
if not os . path . exists ( iiiii ) and IIi1IiiiI1Ii != '' and I11i11Ii != '' : O0o0O00Oo0o0 ( )
elif IIi1IiiiI1Ii == '' and I11i11Ii == '' : i1Oo00 ( 'No username or password present' , 'Would you like to input username and password in settings?' , '' , 'open_settings' )
elif IIi1I11I1II == None : I1i1I ( )
elif IIi1I11I1II == 1 : Ii1i11IIii1I ( oOOoOooOo )
elif IIi1I11I1II == 2 : o0O00oOoOO ( oOOoOooOo , OOooo0O00o )
elif IIi1I11I1II == 3 : O0o0O00Oo0o0 ( )
elif IIi1I11I1II == 4 : Iii111II ( )
elif IIi1I11I1II == 5 : O00OooO0 ( oOOoOooOo , OOooo0O00o , O00ooooo00 )
if 48 - 48: i1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
