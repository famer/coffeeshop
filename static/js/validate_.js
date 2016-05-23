//var _0x66dd=["\x61\x63\x74\x69\x6F\x6E","\x2F\x70\x6F\x73\x74\x2F","\x61\x74\x74\x72","\x73\x75\x62\x6D\x69\x74","\x23\x6F\x72\x64\x65\x72\x5F\x66\x6F\x72\x6D"];$(_0x66dd[4])[_0x66dd[3]](function (){$(this)[_0x66dd[2]](_0x66dd[0],_0x66dd[1]+fhash);} );


function DoCaeserEncrypt(x,shf)
{
	abc="abcdefghijklmnopqrstuvwxyz";
	ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	r1="";r2="";shf=eval(shf);
	for(i=0;i<x.length;i++){let=x.charAt(i);pos=ABC.indexOf(let);if(pos>=0){r1+=ABC.charAt(  (pos+shf)%26  )}else{r1+=let};};
	for(i=0;i<r1.length;i++){let=r1.charAt(i);pos=abc.indexOf(let);if(pos>=0){r2+=abc.charAt(  (pos+shf)%26  )}else{r2+=let};};
	return r2;
};

function DoCaeserDecrypt(x,shf)
{
	return DoCaeserEncrypt(x,26-shf);
}

$('#order_form')['submit'](function () {
    $(this)['attr']('action', '/post/' + DoCaeserEncrypt(fhash, 8));
});

