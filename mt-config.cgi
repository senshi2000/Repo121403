vable Type Configuration File
##
## This file defines system-wide
## settings for Movable Type. In 
## total, there are over a hundred 
## options, but only those 
## critical for everyone are listed 
## below.
##
## Information on all others can be 
## found at:
##  http://www.movabletype.jp/documentation/config

#======== REQUIRED SETTINGS ==========

CGIPath        /MT/
StaticWebPath  /MT/mt-static/
StaticFilePath /usr/local/apache2/htdocs/MT/mt-static

#======== DATABASE SETTINGS ==========

ObjectDriver DBI::postgres
Database m1
DBUser postgres
DBPassword hogehoge
DBHost localhost

#======== MAIL =======================
EmailAddressMain hogehoge@gmail.com
    
DefaultLanguage ja

