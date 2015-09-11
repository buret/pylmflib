#! /usr/bin/env perl
# -*- coding: utf-8 -*-

use strict;
use warnings;
use utf8;

unless (caller) {
    my $input_filename = $ARGV[0];
    my $output_filename = $ARGV[1];
    main($input_filename, $output_filename);
    1;
}

sub consonant {
    $_[0] =~ s/$_[1]$/$_[2]्/g;
    $_[0] =~ s/$_[1] /$_[2]् /g;
    $_[0] =~ s/$_[1]ʌ/$_[2]/g;
    $_[0] =~ s/$_[1]([ा,ि,ी,ु,ू,े,ो,ै,ौ])/$_[2]$1/g;
    $_[0] =~ s/$_[1]/$_[2]्/g;
    $_[0] =~ s/$_[1]/$_[2]्/g;
}

sub vowel {
    my ($radical) = shift;
    $radical =~ tr/uʉi/ʌʌʌ/;
    $radical =~ s/o/oɔ/;
    $radical =~ s/ɵ/oɔ/;
    return $radical;
}

sub infinitive1 {
    my ($radical) = shift;
    $radical =~ s/(k|p|t|r|l|n|m|ŋ)(t|d)/$1/; # simplifies final consonant
    my $variable = $radical;

    if ($radical =~ m/p$/) { # final -p
        $variable =~ s/p$/̂m/;
        $variable = vowel($variable);
    }

    if ($radical =~ m/t$/) { # final -t
        $variable =~ s/t$/̂n/;
        $variable = vowel($variable);
    }

    if ($radical =~ m/k$/) { # final -k
        $variable =~ s/k$/̂ː/;
        $variable =~ tr/iɵʉ/uou/;
    }

    if ($radical =~ m/ŋ$/) { # final -ŋ
        $variable =~ s/ŋ$/ː/;
        $variable =~ tr/iɵʉ/uou/;
    }

    if ($radical =~ m/n$/) { # final -n
        $variable = vowel($variable);
        $variable =~ s/n$/i/;
    }

    if ($radical =~ m/(m|r|l)$/) { # final -r l m
        $variable = vowel($variable);
    }

    $variable =~ tr/A/ɵ/;

    return $variable;
}

sub infinitive2 {
    my ($radical) = shift;
    $radical =~ s/\-si//;
    $radical =~ s/(k|p|t|r|l|n|m|ŋ)(t|d)/$1/; # simplifies final consonant
    my $variable = $radical;
    
    if ($radical =~ m/(m|p|r|l|t|n)$/) {
        $variable = infinitive1($variable);
    }
    
    if ($radical =~ m/k$/) {
        $variable =~ tr/iɵʉ/uou/;
        $variable =~ s/k$/̂n/;
    }
    
    if ($radical =~ m/ŋ$/) {
        $variable =~ tr/iɵʉ/ʌou/;
        $variable =~ s/ŋ$/n/;
    }
    
    if ($radical =~ m/(a|ɛ|i|o|u|ɵ|ʉ|A)$/) {
        $variable =~ tr/ouA/ɵʉɵ/;
        $variable = $variable."̂n";
    }
    
    return $variable."si";
}

sub infinitive {
    my ($radical) = shift;
    my $variable = $radical;
    if ($radical =~ m/\-si$/) { # reflexives
        $variable = infinitive2($variable);
    }
    else {
        $variable = infinitive1($variable);
    }
    return $variable."nɛ";
}

sub transcr {
    my $string = $_[0];

    $string =~ s/ʔɛ̂i([ptkbdgmʦʣɦnŋlrsjw\W])/अ्या:इ$1/g;
    $string =~ s/ʔɛ̄i([ptkbdgmʦʣɦnŋlrsjw\W])/अ्याइ$1/g;
    $string =~ s/ʔɛi([ptkbdgmʦʣɦnŋlrsjw\W])/अ्याइ$1/g;
    $string =~ s/ʔɛ̄ː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsjw\W])/अ्याऽ$1/g;
    $string =~ s/ʔɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/या:$1/g;
    $string =~ s/ʔɛː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsjw\W])/अ्याऽ$1/g;
    $string =~ s/ʔɛ̂([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या:$1/g;
    $string =~ s/ʔɛ̄([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या$1/g;
    $string =~ s/ʔɛ([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या$1/g;
    $string =~ s/ʔɛː/अ्या/g;
    $string =~ s/ʔɛ̄ː/अ्या/g;
    $string =~ s/ʔɛ̂ː/अ्या:/g;
    $string =~ s/ʔɛ/अ्य/g;
    $string =~ s/ɛu/याउ/g;
    $string =~ s/ɛ‍̄u/याउ/g;
    $string =~ s/ɛː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/याऽ$1/g;
    $string =~ s/ɛ̄ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/याऽ$1/g;
    $string =~ s/ɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या:$1/g;
    $string =~ s/ɛ̂i([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/या:इ$1/g;
    $string =~ s/ɛ̄i([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/याइ$1/g;
    $string =~ s/ɛi([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/याइ$1/g;
    $string =~ s/ɛ̂([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या:$1/g;
    $string =~ s/ɛ̄([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या$1/g;
    $string =~ s/ɛ([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या$1/g;
    $string =~ s/ɛː/या/g;
    $string =~ s/ɛ̄ː/या/g;
    $string =~ s/ɛ̂ː/या:/g;
    $string =~ s/ɛ/य/g;

    $string =~ s/ʔʌi/ऐ/g;
    $string =~ s/ʔʌ̄i/ऐ/g;
    $string =~ s/ʔʌ̂i/ऐ:/g;
    $string =~ s/ʔʌu/औ/g;
    $string =~ s/ʔʌ̄u/औ/g;
    $string =~ s/ʔʌ̂u/औ:/g;
    $string =~ s/ʌi/ै/g;
    $string =~ s/ʌ̄i/ै/g;
    $string =~ s/ʌ̂i/ै:/g;
    $string =~ s/ʌu/ौ/g;
    $string =~ s/ʌ̄u/ौ/g;
    $string =~ s/ʌ‍̂u/ौ:/g;
    $string =~ s/īu/िउ/g;
    $string =~ s/iu/िउ/g;
    $string =~ s/ēu/ेउ/g;
    $string =~ s/eu/ेउ/g;
    $string =~ s/ōu/ोउ/g;
    $string =~ s/ou/ोउ/g;

    $string =~ s/̄i/̄इ/g;
    $string =~ s/̂i/̂इ/g;
    $string =~ s/([aeɛiouɵʉʌɔ])i/$1इ/g;

    $string =~ s/ʔʌ/अ/g;
    $string =~ s/ʔoɔ/अ्वा/g;
    $string =~ s/ʔâː/आ:/g;
    $string =~ s/ʔāː/आ/g;
    $string =~ s/ʔaː/आ/g;
    $string =~ s/ʔa/आ/g;
    $string =~ s/ʔoɔ̂/अ्वा:/g;
    $string =~ s/âː/ा:/g;
    $string =~ s/aː/ा/g;
    $string =~ s/āː/ा/g;
    $string =~ s/aː/ा/g;
    $string =~ s/a/ा/g;
    $string =~ s/oɔ̂/वा:/g;
    $string =~ s/oɔ̄/वा/g;
    $string =~ s/oɔ/वा/g;

    $string =~ s/ʔīː/इऽ/g;
    $string =~ s/ʔiː/इऽ/g;
    $string =~ s/ʔîː/इ:/g;
    $string =~ s/ʔi/इ/g;
    $string =~ s/īː/िऽ/g;
    $string =~ s/iː/िऽ/g;
    $string =~ s/îː/ि:/g;
    $string =~ s/i/ि/g;

    $string =~s/ʔʉ/अ्यu/g;
    $string =~s/ʉ/यu/g;

    $string =~s/ʔɵ/अ्यo/g;
    $string =~s/ɵ/यo/g;

    $string =~ s/ʔūː/ऊ/g;
    $string =~ s/ʔuː/ऊ/g;
    $string =~ s/ʔûː/ऊ:/g;
    $string =~ s/ʔu/उ/g;
    $string =~ s/ūː/ुऽ/g;
    $string =~ s/uː/ुऽ/g;
    $string =~ s/ûː/ु:/g;
    $string =~ s/u/ु/g;

    $string =~ s/ʔēː/एऽ/g;
    $string =~ s/ʔêː/ए:/g;
    $string =~ s/ʔe/ए/g;
    $string =~ s/ēː/ेऽ/g;
    $string =~ s/eː/ेऽ/g;
    $string =~ s/êː/े:/g;
    $string =~ s/e/े/g;

    $string =~ s/ʔoː/ओऽ/g;
    $string =~ s/ʔōː/ओऽ/g;
    $string =~ s/ʔôː/ओ:/g;
    $string =~ s/ʔo/ओ/g;
    $string =~ s/ōː/ोऽ/g;
    $string =~ s/oː/ोऽ/g;
    $string =~ s/ôː/ो:/g;
    $string =~ s/o/ो/g;

    $string =~ s/̂/:/g;
    $string =~ s/̄//g;

    &consonant($string,"kh","ख");
    &consonant($string,"k","क");
    &consonant($string,"gh","घ");
    &consonant($string,"g","ग");
    &consonant($string,"ŋ","ङ");

    &consonant($string,"ʦh","छ");
    &consonant($string,"ʦ","च");
    &consonant($string,"ʣh","झ");
    &consonant($string,"ʣ","ज");
    &consonant($string,"ɲ","ञ");

    &consonant($string,"ʈh","ठ");
    &consonant($string,"ʈ","ट");
    &consonant($string,"ɖh","झ");
    &consonant($string,"ɖ","ड");
    &consonant($string,"ɳ","ण");

    &consonant($string,"th","थ");
    &consonant($string,"t","त");
    &consonant($string,"dh","ध");
    &consonant($string,"d","द");
    &consonant($string,"n","न");

    &consonant($string,"ph","फ");
    &consonant($string,"p","प");
    &consonant($string,"bh","भ");
    &consonant($string,"b","ब");
    &consonant($string,"m","म");
    &consonant($string,"ç","ह्इ");

    &consonant($string,"r","र");
    &consonant($string,"l","ल");
    &consonant($string,"s","स");
    &consonant($string,"w","व");
    &consonant($string,"j","य");
    &consonant($string,"ɦ","ह");

    $string =~ s/ह्इ्/ह्इ/g;
    $string =~ s/प्त/प्‍त/g;
    $string =~ s/र्य/र्‍य/g;
    $string =~ s/र्व/र्‍व/g;
    $string =~ s/क्र्‍य/क्र्य/g; # undo previous rules in clusters
	$string =~ s/क्र्‍व/क्र्व/g;
    $string =~ s/ख्र्‍य/ख्र्य/g; 	
	$string =~ s/ख्र्‍व/ख्र्व/g;
    $string =~ s/ग्र्‍य/ग्र्य/g; 
	$string =~ s/ग्र्‍व/ग्र्व/g;
    $string =~ s/घ्र्‍य/घ्र्य/g; 
	$string =~ s/घ्र्‍व/घ्र्व/g;
    $string =~ s/प्र्‍य/प्र्य/g; 	
	$string =~ s/प्र्‍व/प्र्व/g;
	$string =~ s/फ्र्‍य/फ्र्य/g; 	
	$string =~ s/फ्र्‍व/फ्र्व/g;
	$string =~ s/ब्र्‍य/ब्र्य/g; 	
	$string =~ s/ब्र्‍व/ब्र्व/g;
    $string =~ s/भ्र्‍य/भ्र्य/g; 	
	$string =~ s/भ्र्‍व/भ्र्व/g;
    $string =~ s/त्न/त्‍न/g;
    $string =~ s/म्न/म्‍न/g;
    $string =~ s/प्न/प्‍न/g;
    $string =~ s/न्न/न्‍न/g;
    $string =~ s/क्न/क्‍न/g;
    $string =~ s/स्न/स्‍न/g;
    $string =~ s/च्न/च्‍न/g;
    $string =~ s/च्च/च्‍च/g;
    $string =~ s/क्ल/क्‍ल/g;
    $string =~ s/प्ल/प्‍ल/g;
    $string =~ s/ल्ल/ल्‍ल/g;
    $string =~ s/क्व/क्‍व/g;
    $string =~ s/ख्व/ख्‍व/g;
    $string =~ s/द्व/द्‍व/g;
    $string =~ s/च्व/च्‍व/g;
#	$string =~ s/अ्वा/अ\\skt\{्\}वा/g;
#	$string =~ s/अ्य/अ\\skt\{्\}य/g;  
#	$string =~ s/्ये/\\mgl\{्\}ये/g;
#	$string =~ s/ुक्त/\\skt\{ुक्\}त/g;
#	$string =~ s/ुक्क/\\skt\{ुक्\}क/g;
#	$string =~ s/ुङ्/ुङ\\mgl\{्\}/g;
	$string =~ s/क्त/क्\x{200C}त/g;
	$string =~ s/क्क/क्\x{200C}क/g;
	$string =~ s/क्च/क्‍च/g;
	$string =~ s/क्छ/क्‍छ/g;
	$string =~ s/क्म/क्‍म/g;
	$string =~ s/ङ्/ङ्\x{200C}/g;
    $string =~ s/ह्य/ह्‍य/g;
    $string =~ s/द्य/द्\x{200C}य/g;
    $string =~ s/ह्व/ह्‍व/g;
    $string =~ s/\.$/ ।/g;
    $string =~ s/्\-/्\x{200C}/g;
    $string =~ s/-//g;
    $string =~ s/्\./्\x{200C}/g; # unpredictable syllable breaks
	$string =~ s/\.//g; 
    $string =~ tr/[A-Z]/[a-z]/; # conversion of paradigm tables generated with paradigms.pl
	$string =~ tr/\[h\]/\[H\]/;

    return $string;
}

sub main {
    open in_file, "<:utf8", $_[0];
    open out_file, ">:utf8", $_[1];
    my $rime = "";
    my $adv = "";
    while (<in_file>) {
        print out_file $_;
        my ($data) = $_;
        if ($^O =~ "darwin") {
            $data = substr($data, 0, -2); # removes '\r\n' characters on Mac
        }
        else {
            chomp($data);
        }

        if ($data =~ m/^\\lx /) {
            if ($data =~ m/\_/) { # verbs which we do not analyze the infinitive
                $data =~ s/\\lx//;
                $data =~ s/ //;
                $data =~ s/\_//;
                print out_file "\\lx_dev ".transcr($data)."\n";
            }
            else {
                $data =~ s/\\lx//;
                $data =~ s/ //;
                if ($data =~ m/\)/) { # separates the adverb from the verbal root
                    $adv = $data;
                    $adv =~ s/.*\((.*)\).*/$1/;
                    $adv = $adv." ";
                    $data =~ s/(\(.*\))//;
                }
                else {
                    $adv = "";
                }
                $data =~ s/ //;
                $rime = $data;
                my $root = $data;
                $data =~ s/([aeiouɛʌɵʉ])ː/$1̄ː/g;
                $data =~ s/([aeiouɛʌɵʉ])([rlmnŋ])/$1̄$2/g;
                if ($rime =~ m/\-si/) {
                    $rime  =~ s/\-si//;
                    $rime  =~ s/(k|p|t|m|n|ŋ|r|l)t/$1/; # deletes second t
                }
                $rime =~ s/A/a/;
                $rime  =~ s/.*([aeiouɵʉɛ])/$1/; # removal of initial consonants
                $rime  =~ tr/ɵʉ/ou/;
                print out_file "\\lx_tmp ".$root."\n";
                print out_file "\\lc ".$adv.infinitive($data)."\n";
                print out_file "\\lc_dev ".transcr($adv.infinitive($data))."\n";
            }
        }

        if ($data =~ m/^\\se /) {
            $data =~ s/\\se//;
            $data =~ s/ //;
            if ($data =~ m/\)/) {
                $adv = $data;
                $adv =~ s/.*\((.*)\).*/$1/;
                $adv = $adv." ";
                $data =~ s/(\(.*\))//;
            }
            else {
                $adv = "";
            }
            $data =~ s/ //;
            $rime = $data;
            $data =~ s/([aeiouɛʌɵʉ])ː/$1̄ː/g;
            $data =~ s/([aeiouɛʌɵʉ])([rlmnŋ])/$1̄$2/g;
            $rime =~ s/\-si//;
            $rime =~ s/(k|p|t|m|n|ŋ|r|l)t/$1/;
            $rime =~ s/A/a/;
            $rime =~ s/.*([aeiouɵʉɛ])/$1/;
            $rime =~ tr/ɵʉ/ou/;
            print out_file "\\se_tmp ".$data."\n";
            print out_file "\\lc ".$adv.infinitive($data)."\n";
            print out_file "\\lc_dev ".transcr($adv.infinitive($data))."\n";
        }
    
        if ($data =~ m/^\\se2 /) {
            $data =~ s/\\se2//;
            $data =~ s/ //;
            print out_file "\\se2_tmp ".$data."\n";
            print out_file "\\se2_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\xv/) {
            $data =~ s/\\xv//;
            $data =~ s/ //;
            print out_file "\\xv_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\1s/) {
            $data =~ s/\\1s//;
            $data =~ s/ //;
            print out_file "\\1s_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\2s/) {
            $data =~ s/\\2s//;
            $data =~ s/ //;
            print out_file "\\2s_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\3s/) {
            $data =~ s/\\3s//;
            $data =~ s/ //;
            print out_file "\\3s_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\4s/) {
            $data =~ s/\\4s//;
            $data =~ s/ //;
            print out_file "\\4s_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\1d/) {
            $data =~ s/\\1d//;
            $data =~ s/ //;
            print out_file "\\1d_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\3d/) {
            $data =~ s/\\3d//;
            $data =~ s/ //;
            print out_file "\\3d_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\1p/) {
            $data =~ s/\\1p//;
            $data =~ s/ //;
            print out_file "\\1p_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\1e/) {
            $data =~ s/\\1e//;
            $data =~ s/ //;
            print out_file "\\1e_dev ".transcr($data)."\n";
        }

        if ($data =~ m/^\\2p/) {
            $data =~ s/\\2p//;
            $data =~ s/ //;
            print out_file "\\2p_dev ".transcr($data)."\n";
        }
    }
    close(in_file);
    close(out_file);
}
