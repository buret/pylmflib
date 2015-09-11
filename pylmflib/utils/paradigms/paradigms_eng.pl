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
generate_paradigms_eng($input_filename, $output_filename);

my $part1 = "";
my $part2 = "";
my $theme_A = "";
my $theme_B = "";
my $theme_B2 = "";
my $theme_C = "";
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
    $part2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂j/;
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
    $part2 =~ s/([aʌieɛuoɔɵʉ])n/$1j/;
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
    unless (($radical =~ "[aeiouɛɵʉɔʌː]k")|($radical =~ "[aeiouɛɵʉɔʌː]ŋ"))    {
        $radical =~ s/a/ɛ/;
    }
    return $radical;
}

# 2.03
sub rule203 {
    my ($radical) = shift;
    unless (($radical =~ "[aeiouɛɵʉɔʌ]k")|($radical =~ "[aeiouɛɵʉɔʌ]ŋ"))    {
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
    $radical =~ s/([aʌieɛuoɔɵʉ])([mnŋrlj])/$1̂$2/;
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
    $radical =~ s/ː([mnŋrlj])/$1/; # supprimer longueurs en syllabe fermée de sonantes
    $radical =~ s/ː̂([mnŋrlj])/̂$1/;
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

sub generation_eng {
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
    if ((substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]t")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]n")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]nt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]ʦ")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]tt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]s")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːs")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːʦ")) {
        $vowel1 = "";
        $vowel2 = "";
        $vowel3 = "";
    }
    #$result = $result.ipa($theme_A."ŋʌ"."   ".$theme_B."i"." ". $theme_C."ki"." ".$theme_D." ".$theme_E."ni ".$theme_F.$vowel1."ti  ".$theme_H."tɛ")." \n";
    $result = $result."\n";
    $result = $result."\n";

    if ($variable1 =~ /[ptkmnŋrl].i$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vi", "Intransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s &".ipa($theme_A."ŋʌ"." &".$theme_F.$vowel2."tʌ")." \\\\ \n";
        $result = $result."1di &".ipa($theme_B."i"." &".$theme_F.$vowel1."ti")."   \\\\\n";
        $result = $result."1de &".ipa($theme_B."u"." &".$theme_F.$vowel3."tu  ")." \\\\ \n";
        $result = $result."1pi &".ipa($theme_C."ki"." &".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."1pe &".ipa($theme_C."kʌ"." &".$theme_C."tʌkʌ  ")." \\\\ \n";
        $result = $result."2s &".ipa(" ʔi".$theme_D." & ʔi".$theme_G2."tɛ &".$theme_B2."e ")." \\\\ \n";
        $result = $result."2d &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti &".$theme_B."ije")."    \\\\\n";
        $result = $result."2n &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje ")." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_D." & ".$theme_G2."tɛ  ")." \\\\ \n";
        $result = $result."3d &".ipa(" ".$theme_B."i"." & ".$theme_F.$vowel1."ti  ")." \\\\ \n";
        $result = $result."3n &".ipa(" ".$theme_E."nu  & ".$theme_G."tɛnu")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[aɛeiou].i$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vi", "Intransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s &".ipa($theme_2A."ŋʌ"." &".$theme_2A."ŋʌtʌ")." \\\\ \n";
        $result = $result."1di &".ipa($theme_2A."ji"." &".$theme_2A."̂iti  ")." \\\\\n";
        $result = $result."1de &".ipa($theme_2A."ju"." &".$theme_2A."̂itu  ")." \\\\ \n";
        $result = $result."1pi &".ipa($theme_2A."ki"." &".$theme_2A."ktiki  ")." \\\\ \n";
        $result = $result."1pe &".ipa($theme_2A."kʌ"." &".$theme_2A."ktʌkʌ  ")." \\\\ \n";
        $result = $result."2s &".ipa(" ʔi".$theme_2A." & ʔi".$theme_2B."tɛ &".$theme_2B."je ")." \\\\ \n";
        $result = $result."2d &".ipa(" ʔi".$theme_2A."ji"." & ʔi".$theme_2A."̂iti &".$theme_B."̂ije   ")." \\\\\n";
        $result = $result."2n &".ipa(" ʔi".$theme_2A."ni  & ʔi".$theme_2B2."tnu &".$theme_2B2."̂nje ")." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_2A." & ".$theme_2B."tɛ  ")." \\\\ \n";
        $result = $result."3d &".ipa(" ".$theme_2A."ji"." & ".$theme_2A."̂iti    ")." \\\\ \n";
        $result = $result."3n &".ipa(" ".$theme_2A."nu  & ".$theme_2B2."tnu")." \\\\ \n";
        $result = $result.end();
    }

    if ($variable1 =~ /[ptkmnŋrl]t_t$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s>3s &".ipa($theme_O."u"." &".$theme_N."tʌ")." \\\\ \n";
        $result = $result."1s>3d &".ipa($theme_O."usu"." &".$theme_N."tʌsu")." \\\\ \n";
        $result = $result."1s>3p &".ipa($theme_O."unu"." &".$theme_N."tʌnu")." \\\\ \n";
        $result = $result."1di>3 &".ipa($theme_B."i"." &".$theme_F.$vowel1."ti  ")." \\\\\n";
        $result = $result."1de>3 &".ipa($theme_B."u"." &".$theme_F.$vowel3."tu  ")." \\\\ \n";
        $result = $result."1pi>3 &".ipa($theme_C."ki"." &".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."1pe>3 &".ipa($theme_C."kʌ"." &".$theme_C."tʌkʌ  ")." \\\\ \n";
        $result = $result."2s>3s &".ipa(" ʔi".$theme_O."ʉ  & ʔi".$theme_N."tɛ &".$theme_O."e ")." \\\\ \n";
        $result = $result."2s>3d &".ipa(" ʔi".$theme_N."su  & ʔi".$theme_N."tɛsu  ")." \\\\ \n";
        $result = $result."2s>3p &".ipa(" ʔi".$theme_N."nu  & ʔi".$theme_N."tɛnu  ")." \\\\ \n";
        $result = $result."2d>3 &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti &".$theme_B."ije   ")." \\\\\n";
        $result = $result."2n>3 &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje ")." \\\\ \n";
        $result = $result."3s>3s &".ipa(" ".$theme_O."ʉ  & ".$theme_N."tɛ ")." \\\\ \n";
        $result = $result."3>3(d) &".ipa(" ".$theme_N."su"." & ".$theme_N."tɛsu ")." \\\\ \n";
        $result = $result."3>3(p) &".ipa(" ".$theme_N."nu  & ".$theme_N."tɛnu")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."2/3s>1s &".ipa("ʔi".$theme_A."ŋʌ"." &ʔi".$theme_F.$vowel2."tʌ &".$theme_B."ʌje")." \\\\ \n";
        $result = $result."2/3d>1s &".ipa("ʔi".$theme_A."ŋʌsu"." &ʔi".$theme_F.$vowel2."tʌsu &".$theme_B."ʌsuje")." \\\\ \n";
        $result = $result."2/3p>1s &".ipa("ʔi".$theme_A."ŋʌnu"." &ʔi".$theme_F.$vowel2."tʌnu &".$theme_B."ʌnuje")." \\\\ \n";
        $result = $result."2/3>1di &".ipa("ʔi".$theme_B."i"." &ʔi".$theme_F.$vowel1."ti   ")." \\\\\n";
        $result = $result."2/3>1de &".ipa("ʔi".$theme_B."u"." &ʔi".$theme_F.$vowel3."tu  &".$theme_B."uje ")." \\\\ \n";
        $result = $result."2/3>1pi &".ipa("ʔi".$theme_C."ki"." &ʔi".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."2/3>1pe &".ipa("ʔi".$theme_C."kʌ"." &ʔi".$theme_C."tʌkʌ  &".$theme_C."kʌje ")." \\\\ \n";
        $result = $result."3>2s, 1d/pe>2s &".ipa(" ʔi".$theme_D." & ʔi".$theme_G2."tɛ  ")." \\\\ \n";
        $result = $result."3>2d, 1d/pe>2d &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti   ")." \\\\\n";
        $result = $result."3>2p, 1d/pe>2p &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu ")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."1s>2s &".ipa(" ".$theme_E."nɛ  & ".$theme_P."tɛni ")." \\\\ \n";
        $result = $result."1s>2d &".ipa(" ".$theme_M."su  & ".$theme_P."tɛnsu  ")." \\\\ \n";
        $result = $result."1s>2p &".ipa(" ".$theme_M."nu  & ".$theme_P."tɛnnu  ")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[ptkmnŋrl]_t$/) {
        #$result = $result.ipa($theme_H."u ".$theme_I."ʉ  ". $theme_J."nu ".$theme_K.$vowel3."ta ".$theme_L."tɛ " .$theme_M."su")." \n";
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s>3s &".ipa($theme_H."u"." &".$theme_K.$vowel3."tʌ")." \\\\ \n";
        $result = $result."1s>3d &".ipa($theme_H."usu"." &".$theme_K.$vowel3."tʌsu")." \\\\ \n";
        $result = $result."1s>3p &".ipa($theme_H."unu"." &".$theme_K.$vowel3."tʌnu")." \\\\ \n";
        $result = $result."1di>3 &".ipa($theme_B."i"." &".$theme_F.$vowel1."ti  ")." \\\\\n";
        $result = $result."1de>3 &".ipa($theme_B."u"." &".$theme_F.$vowel3."tu  ")." \\\\ \n";
        $result = $result."1pi>3 &".ipa($theme_C."ki"." &".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."1pe>3 &".ipa($theme_C."kʌ"." &".$theme_C."tʌkʌ  ")." \\\\ \n";
        $result = $result."2s>3s &".ipa(" ʔi".$theme_I."ʉ  & ʔi".$theme_L."tɛ &".$theme_I."e ")." \\\\ \n";
        $result = $result."2s>3d &".ipa(" ʔi".$theme_J."su  & ʔi".$theme_L."tɛsu  ")." \\\\ \n";
        $result = $result."2s>3p &".ipa(" ʔi".$theme_J."nu  & ʔi".$theme_L."tɛnu  ")." \\\\ \n";
        $result = $result."2d>3 &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti &".$theme_B."ije   ")." \\\\\n";
        $result = $result."2n>3 &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje ")." \\\\ \n";
        $result = $result."3s>3s &".ipa(" ".$theme_I."ʉ  & ".$theme_L."tɛ ")." \\\\ \n";
        $result = $result."3>3(d) &".ipa(" ".$theme_J."su"." & ".$theme_L."tɛsu ")." \\\\ \n";
        $result = $result."3>3(p) &".ipa(" ".$theme_J."nu  & ".$theme_L."tɛnu")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."2/3s>1s &".ipa("ʔi".$theme_A."ŋʌ"." & ʔi".$theme_F.$vowel2."tʌ &".$theme_B."ʌje")." \\\\ \n";
        $result = $result."2/3d>1s &".ipa("ʔi".$theme_A."ŋʌsu"." & ʔi".$theme_F.$vowel2."tʌsu &".$theme_B."ʌsuje")." \\\\ \n";
        $result = $result."2/3p>1s &".ipa("ʔi".$theme_A."ŋʌnu"." & ʔi".$theme_F.$vowel2."tʌnu &".$theme_B."ʌnuje")." \\\\ \n";
        $result = $result."2/3>1di &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti   ")." \\\\\n";
        $result = $result."2/3>1de &".ipa(" ʔi".$theme_B."u"." & ʔi".$theme_F.$vowel3."tu  &".$theme_B."uje ")." \\\\ \n";
        $result = $result."2/3>1pi &".ipa(" ʔi".$theme_C."ki"." & ʔi".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."2/3>1pe &".ipa(" ʔi".$theme_C."kʌ"." & ʔi".$theme_C."tʌkʌ  &".$theme_C."kʌje ")." \\\\ \n";
        $result = $result."3>2s, 1d/pe>2s &".ipa(" ʔi".$theme_D." & ʔi".$theme_G2."tɛ  ")." \\\\ \n";
        $result = $result."3>2d, 1d/pe>2d &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti   ")." \\\\\n";
        $result = $result."3>2p, 1d/pe>2p &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu ")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."1s>2s &".ipa(" ".$theme_E."nɛ  & ".$theme_P."tɛni ")." \\\\ \n";
        $result = $result."1s>2d &".ipa(" ".$theme_M."su  & ".$theme_P."tɛnsu  ")." \\\\ \n";
        $result = $result."1s>2p &".ipa(" ".$theme_M."nu  & ".$theme_P."tɛnnu  ")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[aeiou]_t$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s &".ipa($theme_2D."ŋʌ"." &".$theme_2E."̂ŋtʌ")." \\\\ \n";
        $result = $result."1di &".ipa($theme_2C."ji"." &".$theme_2C."̂iti  ")." \\\\\n";
        $result = $result."1de &".ipa($theme_2C."ju"." &".$theme_2C."̂itu  ")." \\\\ \n";
        $result = $result."1pi &".ipa($theme_2C."ki"." &".$theme_2C."ktiki  ")." \\\\ \n";
        $result = $result."1pe &".ipa($theme_2C."kʌ"." &".$theme_2C."ktʌkʌ  ")." \\\\ \n";
        $result = $result."2s &".ipa(" ʔi".$theme_2A." & ʔi".$theme_2F."tɛ &".$theme_2F."je ")." \\\\ \n";
        $result = $result."2d &".ipa(" ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti &".$theme_2C."̂ije   ")." \\\\\n";
        $result = $result."2n &".ipa(" ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu &".$theme_2G2."̂nje ")." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_2A." & ".$theme_2F."tɛ  ")." \\\\ \n";
        $result = $result."3d &".ipa(" ".$theme_2A."su"." & ".$theme_2F."tsu    ")." \\\\ \n";
        $result = $result."3n &".ipa(" ".$theme_2A."nu  & ".$theme_2F."tnu")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."2/3s>1s &".ipa("ʔi".$theme_2C."ŋʌ"." &ʔi".$theme_2C."ŋʌtʌ &".$theme_2C."ŋʌje")." \\\\ \n";
        $result = $result."2/3d>1s &".ipa("ʔi".$theme_2C."ŋʌsu"." &ʔi".$theme_2C."ŋʌtʌsu &".$theme_2C."ŋʌsuje")." \\\\ \n";
        $result = $result."2/3p>1s &".ipa("ʔi".$theme_2C."ŋʌnu"." &ʔi".$theme_2C."ŋʌtʌnu &".$theme_2C."ŋʌnuje")." \\\\ \n";
        $result = $result."2/3>1di &".ipa("ʔi".$theme_2C."ji"." &ʔi".$theme_2C."̂iti   ")." \\\\\n";
        $result = $result."2/3>1de &".ipa("ʔi".$theme_2C."ju"." &ʔi".$theme_2C."̂itu  &".$theme_2C."ije ")." \\\\ \n";
        $result = $result."2/3>1pi &".ipa("ʔi".$theme_2C."ki"." &ʔi".$theme_2C."ktiki  ")." \\\\ \n";
        $result = $result."2/3>1pe &".ipa("ʔi".$theme_2C."kʌ"." &ʔi".$theme_2C."ktʌkʌ  &".$theme_2C."kʌje ")." \\\\ \n";
        $result = $result."3>2s, 1d/pe>2s &".ipa(" ʔi".$theme_2C." & ʔi".$theme_2G."tɛ  ")." \\\\ \n";
        $result = $result."3>2d, 1d/pe>2d &".ipa(" ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti    ")." \\\\\n";
        $result = $result."3>2p, 1d/pe>2p &".ipa(" ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu ")." \\\\ \n";
        $result = $result."\\midrule\n";
        $result = $result."1s>2s &".ipa(" ".$theme_2C."nɛ  & ".$theme_2C."̂ntɛni ")." \\\\ \n";
        $result = $result."1s>2d &".ipa(" ".$theme_2C."̂nsu  & ".$theme_2C."̂ntɛnsu  ")." \\\\ \n";
        $result = $result."1s>2p &".ipa(" ".$theme_2C."̂nnu  & ".$theme_2C."̂ntɛnnu  ")." \\\\ \n";
        $result = $result.end();
    }

    if ($variable1 =~ /[ptkmnŋrl]t_1$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s>3s &".ipa($theme_O."u"." &".$theme_N."tʌ")." \\\\ \n";
        $result = $result."1s>3d &".ipa($theme_O."usu"." &".$theme_N."tʌsu")." \\\\ \n";
        $result = $result."1s>3p &".ipa($theme_O."unu"." &".$theme_N."tʌnu")." \\\\ \n";
        $result = $result."1di>3 &".ipa($theme_B."i"." &".$theme_F.$vowel1."ti  ")." \\\\\n";
        $result = $result."1de>3 &".ipa($theme_B."u"." &".$theme_F.$vowel3."tu  ")." \\\\ \n";
        $result = $result."1pi>3 &".ipa($theme_C."ki"." &".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."1pe>3 &".ipa($theme_C."kʌ"." &".$theme_C."tʌkʌ  ")." \\\\ \n";
        $result = $result."2s>3s &".ipa(" ʔi".$theme_O."ʉ  & ʔi".$theme_N."tɛ &".$theme_O."e ")." \\\\ \n";
        $result = $result."2s>3d &".ipa(" ʔi".$theme_N."su  & ʔi".$theme_N."tɛsu  ")." \\\\ \n";
        $result = $result."2s>3p &".ipa(" ʔi".$theme_N."nu  & ʔi".$theme_N."tɛnu  ")." \\\\ \n";
        $result = $result."2d>3 &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti &".$theme_B."ije   ")." \\\\\n";
        $result = $result."2n>3 &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje ")." \\\\ \n";
        $result = $result."3s>3s &".ipa(" ".$theme_O."ʉ  & ".$theme_N."tɛ ")." \\\\ \n";
        $result = $result."3>3(d) &".ipa(" ".$theme_N."su"." & ".$theme_N."tɛsu ")." \\\\ \n";
        $result = $result."3>3(p) &".ipa(" ".$theme_N."nu  & ".$theme_N."tɛnu")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[ptkmnŋrl]_1$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s>3s &".ipa($theme_H."u"." &".$theme_K.$vowel3."tʌ")." \\\\ \n";
        $result = $result."1s>3d &".ipa($theme_H."usu"." &".$theme_K.$vowel3."tʌsu")." \\\\ \n";
        $result = $result."1s>3p &".ipa($theme_H."unu"." &".$theme_K.$vowel3."tʌnu")." \\\\ \n";
        $result = $result."1di>3 &".ipa($theme_B."i"." &".$theme_F.$vowel1."ti  ")." \\\\\n";
        $result = $result."1de>3 &".ipa($theme_B."u"." &".$theme_F.$vowel3."tu  ")." \\\\ \n";
        $result = $result."1pi>3 &".ipa($theme_C."ki"." &".$theme_C."tiki  ")." \\\\ \n";
        $result = $result."1pe>3 &".ipa($theme_C."kʌ"." &".$theme_C."tʌkʌ  ")." \\\\ \n";
        $result = $result."2s>3s &".ipa(" ʔi".$theme_I."ʉ  & ʔi".$theme_L."tɛ &".$theme_I."e ")." \\\\ \n";
        $result = $result."2s>3d &".ipa(" ʔi".$theme_J."su  & ʔi".$theme_L."tɛsu  ")." \\\\ \n";
        $result = $result."2s>3p &".ipa(" ʔi".$theme_J."nu  & ʔi".$theme_L."tɛnu  ")." \\\\ \n";
        $result = $result."2d>3 &".ipa(" ʔi".$theme_B."i"." & ʔi".$theme_F.$vowel1."ti &".$theme_B."ije   ")." \\\\\n";
        $result = $result."2n>3 &".ipa(" ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje ")." \\\\ \n";
        $result = $result."3s>3s &".ipa(" ".$theme_I."ʉ  & ".$theme_L."tɛ ")." \\\\ \n";
        $result = $result."3>3(d) &".ipa(" ".$theme_J."su"." & ".$theme_L."tɛsu ")." \\\\ \n";
        $result = $result."3>3(p) &".ipa(" ".$theme_J."nu  & ".$theme_L."tɛnu")." \\\\ \n";
        $result = $result.end();
    }

    if ($variable1 =~ /[aeiou]_1$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Transitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past & imperative"." \\\\ \n";
        $result = $result."1s &".ipa($theme_2D."ŋʌ"." &".$theme_2E."̂ŋtʌ")." \\\\ \n";
        $result = $result."1di &".ipa($theme_2C."ji"." &".$theme_2C."̂iti  ")." \\\\\n";
        $result = $result."1de &".ipa($theme_2C."ju"." &".$theme_2C."̂itu  ")." \\\\ \n";
        $result = $result."1pi &".ipa($theme_2C."ki"." &".$theme_2C."ktiki  ")." \\\\ \n";
        $result = $result."1pe &".ipa($theme_2C."kʌ"." &".$theme_2C."ktʌkʌ  ")." \\\\ \n";
        $result = $result."2s &".ipa(" ʔi".$theme_2A." & ʔi".$theme_2F."tɛ &".$theme_2F."je ")." \\\\ \n";
        $result = $result."2d &".ipa(" ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti &".$theme_2C."̂ije   ")." \\\\\n";
        $result = $result."2n &".ipa(" ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu &".$theme_2G2."̂nje ")." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_2A." & ".$theme_2F."tɛ  ")." \\\\ \n";
        $result = $result."3d &".ipa(" ".$theme_2A."su"." & ".$theme_2F."tsu    ")." \\\\ \n";
        $result = $result."3n &".ipa(" ".$theme_2A."nu  & ".$theme_2F."tnu")." \\\\ \n";
        $result = $result.end();
    }

    if ($variable1 =~ /[ptkmnŋrl]t_2$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Detransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past"." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_O."ʉ  & ".$theme_N."tɛ ")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[ptkmnŋrl]_2$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vt", "Detransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past"." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_O."ʉ  & ".$theme_N."tɛ ")." \\\\ \n";
        $result = $result.end();
    }

    if ($variable1 =~ /[ptkmnŋrl]_3$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vi", "Intransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past"." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_D." & ".$theme_G2."tɛ  ")." \\\\ \n";
        $result = $result.end();
    }
    elsif ($variable1 =~ /[aɛeiou]_3$/) {
        $result = $result.begin_table();
        $result = $result.caption_eng($rime.".vi", "Intransitive verb", $radical, $variable2);
        $result = $result.begin_tabular();
        $result = $result."& non-past & past"." \\\\ \n";
        $result = $result."3s &".ipa(" ".$theme_2A." & ".$theme_2B."tɛ  ")." \\\\ \n";
        $result = $result.end();
    }

    return $result;
}

sub begin_table {
    return "\\begin{table}[H]\n\\centering\n";
}

sub caption_eng{
    return "\\caption{\\label{".$_[0].".eng}. ".$_[1]." \\ipa{".$_[2]."} \"".$_[3]."\" }\n";
}

sub begin_tabular {
    return "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
}

sub end {
    return "\\bottomrule\n\\end{tabular}\n\\end{table}\n";
}

sub ipa {
    my $string = "";
    my @words = split('&', $_[0]);
    foreach my $word (@words) {
        # Delete spaces at the beginning of the word if any
        $word =~ s/^\s+//;
        # Delete spaces at the end of the word if any
        $word =~ s/\s+$//;
        $string = $string."\\ipa{".$word."} & ";
    }
    # Remove last " & " characters
    $string = substr($string, 0, length($string) - 3);
    return $string;
}

sub generate_paradigms_eng {
    open in_file, "<:utf8", $_[0];
    open out_file, ">:utf8", $_[1];
    while (<in_file>) {
        my ($data)= $_;
        chomp($data);
        my @words = split('-', $data);
        print out_file generation_eng($words[0], $words[1]);
    }
    close(in_file);
    close(out_file);
}
