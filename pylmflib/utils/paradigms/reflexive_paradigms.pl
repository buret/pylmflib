#! /usr/bin/env perl
# -*- coding: utf-8 -*-

use strict;
use warnings;
use utf8;

# use module ipa2devanagari.pl
unshift(@INC,"./pylmflib/utils/ipa2devanagari");
require 'ipa2devanagari.pl';

my $input_filename = $ARGV[0];
my $output_filename = $ARGV[1];
generate_reflexive_paradigms($input_filename, $output_filename);

my $part1 = "";
my $part2 = "";
my $theme_A = "";
my $theme_B = "";
my $theme_B2 = "";
my $theme_C = "";
my $theme_C2 = "";
my $theme_D = "";
my $theme_E = "";
my $theme_F = "";
my $theme_G = "";
my $theme_G2 = "";
my $theme_H = "";
my $theme_I = "";
my $theme_J = "";
my $theme_K = "";
my $theme_L = "";
my $theme_M = "";
my $theme_N = "";
my $theme_O = "";
my $theme_P = "";
    
my $theme_2A = "";
my $theme_2B = "";
my $theme_2B2 = "";
my $theme_2C = "";
my $theme_2D = "";
my $theme_2E = "";
my $theme_2F = "";
my $theme_2G = "";
my $theme_2G2 = "";

# 1.01
sub rule101 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-1);
    $part2 = substr($radical,-1,1);
    $part2 =~ tr/[p,t,k]/[b,d,g]/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.02
sub rule102 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1ʦ/;
    $part2 =~ s/([aʌieɛuoɔɵʉ])n/$1ːʦ/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.03
sub rule103 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1s/;
    $part2 =~ s/([aʌieɛuoɔɵʉ])n/$1ːs/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.04
sub rule104 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1ç/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.05
sub rule105 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])p/$1̂m/;
    $part2 =~ s/([aʌeiɛuoɔɵʉ])k/$1̂ŋ/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.06
sub rule106 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂n/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.07
sub rule107 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂i/; # keep an 'i' because it has to be displayed as 'इ'
    $radical = $part1.$part2;
    return $radical;
}

# 1.08
sub rule108 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂ː/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.09
sub rule109 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/([aʌieɛuoɔɵʉ])n/$1i/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.10
sub rule110 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/ik/ûː/;
    $part2 =~ s/([aiʌeɛuoɔɵʉ])k/$1̂ː/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.11
sub rule111 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/iŋ/ūː/;
    $part2 =~ s/([aiʌeɛuoɔɵʉ])ŋ/$1̄ː/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.12
sub rule112 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-2);
    $part2 = substr($radical,-2,2);
    $part2 =~ s/([ptkmnŋrl])t/$1/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.13
sub rule113 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-1);
    $part2 = substr($radical,-1,1);
    $part2 =~ s/ak/a/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.15
sub rule115 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-3);
    $part2 = substr($radical,-3,3);
    $part2 =~ s/iŋt/unt/;
    $part2 =~ s/ŋt/nt/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.16
sub rule116 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-2);
    $part2 = substr($radical,-2,2);
    $part2 =~ s/iŋ/un/;
    $part2 =~ s/ŋ/n/;
    $part2 =~ s/ik/ûn/;
    $part2 =~ s/k/̂n/;
    $radical = $part1.$part2;
    return $radical;
}

# 1.17
sub rule117 {
    my ($radical) = shift;
    $part1 = substr($radical,0,-2);
    $part2 = substr($radical,-2,2);
    $part2 =~ s/([mnŋrl])t/$1d/;
    $radical = $part1.$part2;
    return $radical;
}

# 2.01
sub rule201 {
    my ($radical) = shift;
    $radical =~ s/o/ɵ/;
    $radical =~ s/u/ʉ/;
    return $radical;
}

# 2.02
sub rule202 {
    my ($radical) = shift;
    unless (($radical =~ "[aeiouɛɵʉɔʌː]k")|($radical =~ "[aeiouɛɵʉɔʌː]ŋ")) {
        $radical =~ s/a/ɛ/;
    }
    return $radical;
}

# 2.03
sub rule203 {
    my ($radical) = shift;
    unless (($radical =~ "[aeiouɛɵʉɔʌ]k")|($radical =~ "[aeiouɛɵʉɔʌ]ŋ")) {
        $radical =~ s/i/ʌ/;
        $radical =~ s/u/ʌ/;
        $radical =~ s/o/oɔ/;
    }
    return $radical;
}

# 2.04
sub rule204{
    my ($radical) = shift;
    $radical =~ s/ik/ʌk/;
    $radical =~ s/iŋ/ʌŋ/;
    $radical =~ s/ig/ʌg/;
    $radical =~ s/ɵk/ok/;
    $radical =~ s/ɵŋ/oŋ/;
    $radical =~ s/ɵg/og/;
    $radical =~ s/ʉk/uk/;
    $radical =~ s/ʉŋ/uŋ/;
    $radical =~ s/ʉg/ug/;
    return $radical;
}

# 2.05
sub rule205 {
    my ($radical) = shift;
    $radical =~ s/a/ʌ/;
    return $radical;
}

# 3.01
sub rule301 {
    my ($radical) = shift;
    $radical =~ s/ʌ/aː/;
    $radical =~ s/a/aː/;
    $radical =~ s/o/oː/;
    $radical =~ s/ɵ/ɵː/;
    $radical =~ s/u/uː/;
    $radical =~ s/ʉ/ʉː/;
    $radical =~ s/i/iː/;
    $radical =~ s/e/eː/;
    $radical =~ s/ɛ/ɛː/;
    return $radical;
}

# 3.02
sub rule302 {
    my ($radical) = shift;
    $radical =~ s/([aʌieɛuoɔɵʉ])([mnŋrli])/$1̂$2/;
    return $radical;
}

# 3.03
sub rule303 {
    my ($radical) = shift;
    $radical =~ s/ep/eːp/;
    $radical =~ s/ɛp/ɛːp/;
    return $radical;
}

# 3.04
sub rule304 {
    my ($radical) = shift;
    $radical =~ s/ː([mnŋrl])/$1/; # supprimer longueurs en syllabe fermée de sonantes
    $radical =~ s/ː̂([mnŋrl])/̂$1/;
    $radical =~ s/ːː/ː/;
    $radical =~ s/ː̂ː/̂ː/;
    return $radical;
}

# 4.01
sub rule401 {
    my ($radical) = shift;
    $radical =~ s/([a,e,o,u])/$1ː/;
    $radical =~ s/i/uː/;
    $radical =~ s/ɛ/aː/;
    return $radical;
}

sub generation_reflexive_paradigms {
    my ($variable1) = $_[0];
    my ($variable2) = $_[1];
    my $result = "";

    my $radical = $variable1;
    #$radical =~ s/,[\w|\(|\)|\;|\_|\.]+?,/,/;
    $radical =~ s/\_.//; # remove '_' and all other characters (mark of 'tr' at end of root)
    $radical =~ s/ //;
    my $rime = $radical;
    $rime  =~ s/.*([aeiouɛ])/$1/;

    my $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule107($form);
    $form = rule109($form);
    $form = rule110($form);
    $form = rule111($form);
    $form = rule105($form);
    $theme_A = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule102($form);
    $form = rule201($form);
    $form = rule205($form);
    $theme_B = $form;

    $form =$radical;
    if ($radical =~  /t$/) { # does not go through rule 205
        #$form = rule202($form);
        $form = rule102($form);
        $form = rule201($form);
        $theme_B2 = $form.'ʦ';
    }
    elsif ($radical =~  /n$/) {
        #$form = rule202($form);
        $form = rule102($form);
        $form = rule201($form);
        $theme_B2 = $form;
    }
    else {
        #$form = rule202($form);
        $form = rule201($form);
        $form = rule302($form);
        $theme_B2 = $form.'j';
    }

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule104($form);
    $form = rule109($form);
    $theme_C = $form;

    $form =$radical;
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule109($form);
    $form = rule103($form);
    $theme_C2 = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule110($form);
    $form = rule204($form);
    $form = rule107($form);
    $form = rule109($form);
    $form = rule303($form);
    $theme_D = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule110($form);
    $form = rule111($form);
    $form = rule204($form);
    $form = rule105($form);
    $form = rule106($form);
    $form = rule107($form);
    $form = rule109($form);
    $form = rule303($form);
    $theme_E = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule103($form);
    $form = rule201($form);
    $form = rule205($form);
    $theme_F = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule103($form);
    $form = rule201($form);
    $theme_G = $form;

    $form = rule302($form);
    $theme_G2 = $form;
    
    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule101($form);
    $form = rule205($form);
    $theme_H = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule101($form);
    $form = rule201($form);
    $form = rule301 ($form);
    $theme_I = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule201($form);
    $form = rule302 ($form);
    $form = rule301($form);
    $form = rule304($form);
    $theme_J = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule108($form);
    $form = rule101($form);
    $form = rule205($form);
    $theme_K = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule201($form);
    $form = rule108($form);
    $form = rule302 ($form);
    $form = rule301($form);
    $form = rule304($form);
    $theme_L = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule105($form);
    $form = rule106($form);
    $form = rule107($form);
    $form = rule109($form);
    $form = rule116($form);
    $form = rule302($form);
    $form = rule110($form);
    $theme_M = $form;

    $form =$radical;
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule115($form);
    $form = rule117($form);
    $theme_O = $form;

    $form =$radical;
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule115($form);
    $form = rule112($form);
    $form = rule117($form);
    $form = rule302($form);
    $theme_N = $form;

    $form =$radical;
    $form = rule112($form);
    #$form = rule202($form);
    $form = rule203($form);
    $form = rule204($form);
    $form = rule105($form);
    $form = rule106($form);
    $form = rule107($form);
    $form = rule109($form);
    $form = rule116($form);
    $form = rule110($form);
    $theme_P = $form;

    $form =$radical;
    $form = rule202($form);
    $form = rule201($form);
    $theme_2A = $form;

    $form =$radical;
    $form = rule401($form);
    $theme_2B = $form;

    $theme_2B2 = $theme_2B;
    $theme_2B2 =~ s/ː//;

    $form =$radical;
    $form =~ s/a/o/;
    $form = rule201($form);
    $theme_2C = $form;

    $form =$radical;
    $form =~ s/a/ʌ/;
    $form = rule201($form);
    $theme_2D = $form;

    $form =$radical;
    $form = rule201($form);
    $form =~ s/a/u/;
    $theme_2E = $form;

    $form =$radical;
    $form =~ s/a/u/;
    $form = rule201($form);
    $theme_2F = $form;

    $form =$radical;
    $form =~ s/a/o/;
    $form = rule401($form);
    $theme_2G = $form;

    $theme_2G2 = $theme_2G; # short form
    $theme_2G2 =~ s/ː//;

    my $vowel1 = "i";
    my $vowel2 = "ʌ";
    my $vowel3 = "u";
    if ((substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]t") | (substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]n") | (substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]nt") | (substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]ʦ") | (substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]tt") | (substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]s") | (substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːs") | (substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːʦ")) {
        $vowel1 = "";
        $vowel2 = "";
        $vowel3 = "";
    }
    #$result = $result.transcr($theme_A."ŋʌ"."   ".$theme_B."i"." ". $theme_C."ki"." ".$theme_D." ".$theme_E."ni ".$theme_F.$vowel1."ti  ".$theme_H."tɛ). \n";
    $result = $result."\n\n";

    if ($variable1 =~ /[ptkmnŋrl].r$/) {
        $result = $result.begin_table();
        $result = $result.caption($rime.".vr", "अकर्मक क्रिया  ".$theme_P."sinɛ", $variable2);
        $result = $result.begin_tabular();
        $result = $result.transcr("ʔûŋ &".$theme_P."siŋʌ"." &".$theme_P."tʌsu")." \\\\ \n";
        $result = $result.transcr("ʔīːʦi &".$theme_G."siji"." &".$theme_G."sîiti")."   \\\\\n";
        $result = $result.transcr("ʔōːʦu &".$theme_G."siju"." &".$theme_G."sîitu")."   \\\\ \n";
        $result = $result.transcr("ʔik &".$theme_C2."siki"." &".$theme_C2."siktiki")."   \\\\ \n";
        $result = $result.transcr("ʔok &".$theme_C2."sikʌ"." &".$theme_C2."siktʌkʌ")."   \\\\ \n";
        $result = $result.transcr("ʔin & ʔi".$theme_P."si & ʔi".$theme_P."tɛsi &".$theme_P."sije")."  \\\\ \n";
        $result = $result.transcr("ʔēːʦi & ʔi".$theme_G."siji"." & ʔi".$theme_G."sîːti &".$theme_G."sîije")."    \\\\\n";
        $result = $result.transcr("ʔên & ʔi".$theme_P."sini  & ʔi".$theme_P."tɛnnu &".$theme_P."nuje")."  \\\\ \n";
        $result = $result.transcr("ʔʌ̄m & ".$theme_P."si & ".$theme_P."tɛsi")."   \\\\ \n";
        $result = $result.transcr("ʔʌmsu & ".$theme_G."siji"." & ".$theme_G."sîiti")."   \\\\ \n";
        $result = $result.transcr("ʔʌmɦɛm & ".$theme_P."sinu  & ".$theme_P."tɛnnu")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[aɛeiou]_r$/) {
        $result = $result.begin_table();
        $result = $result."\\caption{\\label{".$rime.".vr} ".transcr("अकर्मक क्रिया  ".$theme_2A."̂nsinɛ  ``").$variable2."\"  }\n";
        $result = $result.begin_tabular();
        $result = $result.transcr("ʔûŋ &".$theme_2A."̂nsiŋʌ"." &".$theme_2A."̂ntʌsu")." \\\\ \n";
        $result = $result.transcr("ʔīːʦi &".$theme_2A."ssiji"." &".$theme_2A."ssîiti")."   \\\\\n";
        $result = $result.transcr("ʔōːʦu &".$theme_2A."ssiju"." &".$theme_2A."ssîitu")."   \\\\ \n";
        $result = $result.transcr("ʔik&".$theme_2A."ssiki"." &".$theme_2A."ssiktiki")."   \\\\ \n";
        $result = $result.transcr("ʔok &".$theme_2A."ssikʌ"." &".$theme_2A."siktʌkʌ")."   \\\\ \n";
        $result = $result.transcr("ʔin & ʔi".$theme_2A."̂ssi & ʔi".$theme_2A."̂ntɛsi &".$theme_2A."̂nsije")."  \\\\ \n";
        $result = $result.transcr("ʔēːʦi & ʔi".$theme_2A."ssiji"." & ʔi".$theme_2A."ssîiti &".$theme_2A."ssîije")."    \\\\\n";
        $result = $result.transcr("ʔên & ʔi".$theme_2A."̂nsini  & ʔi".$theme_2A."̂ntɛnnu &".$theme_2A."̂nnuje")."  \\\\ \n";
        $result = $result.transcr("ʔʌm & ".$theme_2A."̂nsi & ".$theme_2A."̂ntɛsi")."   \\\\ \n";
        $result = $result.transcr("ʔʌmsu & ".$theme_2A."ssiji"." & ".$theme_2A."ssîiti")."   \\\\ \n";
        $result = $result.transcr("ʔʌmɦɛm & ".$theme_2A."̂nsinu  & ".$theme_2A."̂ntɛnnu")." \\\\ \n";
        $result = $result.end();
    }

    return $result;
}

sub begin_table {
    return "\\begin{table}[H]\n\\centering\n";
}

sub caption{
    return "\\caption{\\label{".$_[0]."} ".transcr($_[1])."  \"".$_[2]."\"  }\n";
}

sub begin_tabular {
    return "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
}

sub end {
    return "\\bottomrule\n\\end{tabular}\n\\end{table}\n";
}

sub generate_reflexive_paradigms {
    open in_file, "<:utf8", $_[0];
    open out_file, ">:utf8", $_[1];
    while (<in_file>) {
        my ($data)= $_;
        chomp($data);
        my @words = split('-', $data);
        print out_file generation_reflexive_paradigms($words[0], $words[1]);
    }
    close(in_file);
    close(out_file);
}
