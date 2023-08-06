unicode_ids拡張(日本語版説明書)
===============================

.. note::

   日本語版(本頁)は\ `公式サイト
   <http://h12u.com/sphinx/unicode_ids/README_ja.html>`_\ とこのパッケージの\
   docフォルダでご覧になれます。

.. role:: fn_rst

はじめに
--------
2015年6月4日現在、Sphinx 1.3.1のHTML出力は、id属性に対してASCII限定の文字\
だけを使うように動作します。これはHTML4.01の仕様書に厳密に従おうとするため\
ですが、今日ではUnicodeで定義された文字を使えます。

同様に、ASCII外の文字を名前に持つファイルはSphinx独自の変換を行ってしまい\
ます。このため生成するHTMLファイル名は非常にわかりにくいものになります。

この拡張は、実行のたびにSphinxとその基盤であるdocutilsへパッチをあてる\
形で、指定通りの文字を使わせるようにするものです。

利用条件
--------
Sphinxと同じく二項BSDです。

設置について
------------
他のPythonパッケージと同様に設置・撤去できます。また他のSphinx拡張と同様に\
必要なファイルだけ各自の管理下に複製し、そのフォルダを\ :fn_rst:`conf.py`\
で指定することでも利用いただけます。

動作条件
........
32ビット版のPython 2.7.10と64ビット版のPython 3.4.3をマイクロソフトウィンドウズ
8.1上で動かして挙動を確認しました。特段の依存性はないので、他のPython実装や\
他のOSでも動作すると思います。

Unicodeで定義された全文字への対応はPython 3が必須です。Python 2ではその標準\
符号化法かファイルシステムの符号化法に利用できる文字が限定されます。

また、この拡張はSphinx 1.3.1とdocutils 0.12の実装コード内容に依存しています。\
パッチ先の関数類に互換性のない変更があると動作しなくなります。

設置方法
........
前述の通り、通常のPythonパッケージと同様の方法で設置できます。

#. コンソールを開き\ :code:`pip install unicode_ids`\ を実行してください。

   マイクロソフトウィンドウズでは\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install unicode_ids`\
   を実行してください。

#. あるいは\ :fn_rst:`unicode_ids-2.0.5(.zip)`\ (2.0.5はバージョン番号)\
   というファイルを入手し、このファイルがあるフォルダへ移動した後\
   :code:`pip install unicode_ids-2.0.5.zip`\ を実行してください。

   同様にウィンドウズでは代わりに\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install unicode_ids-2.0.5.zip`\
   を実行してください。

#. 最後の別の方法として、これはSphinx特有の方法ですが、単にzipファイルを任意の\
   フォルダに展開して使うという手段があります。Sphinxで使う\ :fn_rst:`conf.py`\
   を適切に編集することで利用可能です。

使い方
------
他のSphinx拡張同様、\ :fn_rst:`conf.py`\ の編集によって使えるようになります。

まず、次のコードを追加してください:

.. code-block:: python

  # 次の3行を追加してください
  import distutils.sysconfig
  site_package_path = distutils.sysconfig.get_python_lib()
  sys.path.insert(0, os.path.join(site_package_path, 'sphinxcontrib/unicode_ids'))

ただし、もしpipで設置していないのであれば代わりに次を追加してください:

.. code-block:: python

  # 上記のimportやsite_package_pathの二行は使わないのでなくても構いません
  sys.path.insert(0, '<unicode_ids.pyがあるフォルダへのパス>')

次に当拡張を\ :code:`extension`\ に追加してください:

.. code-block:: python

   extension = ['unicode_ids', ] # 他の拡張も無論同時に利用できます

HTMLなどでUnicodeを使って良いと考える根拠
-----------------------------------------
本節は2015年6月4日(日本時間)にかかれています。

本書末に参考文献としてリンクを示しているほか、\
CSSについてはmomdo/もんどさんの\ `CSS3の日本語訳集
<http://momdo.s35.xrea.com/web-html-test/CSS3-ja/>`_\
が便利です。

HTMLにおけるURI一般
...................
HTML4.01 [HTML401J]_\ ではURLに使える文字を\
:code:`A-Za-z0-9_:.`\ および :code:`-`\ に限定しています。

しかし同時に本文中でそれ以外の文字が来たら同処理すべきかについての\
指標も示されており、\
`B.2.1 Non-ASCII characters in URI attribute values
<http://www.w3.org/TR/html401/appendix/notes.html#h-B.2>`_\
節に詳細があります(`B.2.1 URI属性値の非ASCII文字
<http://www.asahi-net.or.jp/~sd5a-ucd/rec-html401j/appendix/notes.html#h-B.2.1>`_)。\
この処理を介してURIをASCIIの7bit文字のみに修正して利用できるという仕組みです。

HTML4.01においてはこの処理、つまり百分率記号を使った符号化は常にUTF-8で\
行うこととする一方、古い文書では他の符号化法によることを期待している\
可能性にも触れています。

HTML5 [HTML5J]_ [HTML51J]_\ においてはもう少しややこしい方法が定義されており、\
`2.5 URLs
<http://www.w3.org/TR/html5/infrastructure.html#urls>`_\
節に詳細があります(`2.5 URL(邦訳)
<http://momdo.github.io/html5/infrastructure.html#urls>`_)。\
もしURLを解析する段階で符号化法が定められていたり、\
もともとのHTML文書がUTF-8以外で符号化されていた場合はそちらのもとにURLを\
再構成することとされています。

両方の仕様を考慮すると、HTMLファイルは常にUTF-8で符号化するのが安全と\
思われます。百分率記号による符号化がいずれにせよUTF-8を前提とできるから\
です。

このほか、W3C URL [W3CURLJ]_\ およびWHATWG URL Living Standard [WHATWGURLJ]_\
という仕様もあり、こちらでも常にUTF-8を使うことを期待する文面があります。

HTMLにおける識別子(アンカー)
............................
HTML5では\ `id attribute <http://www.w3.org/TR/html5/dom.html#the-id-attribute>`_\
を\ `unique identifier
<http://www.w3.org/TR/html5/infrastructure.html#concept-id>`_\ ('一意識別子')\
と定義しています(`3.2.5.1 id属性
<http://momdo.github.io/html5/dom.html#the-id-attribute>`_)。

この語は同書の\
`2.2.2 Dependencies
<http://www.w3.org/TR/html5/infrastructure.html#dependencies>`_\ ('依存先')\
節にて、用語DOMの説明文中でDOM仕様の定義をそのまま運用することとされています。

DOM4 [DOM4J]_\ の\ `5.8 Interface Element
<http://www.w3.org/TR/dom#interface-element>`_\ (`4.8 インターフェイス Element
<http://www.hcn.zaq.ne.jp/___/WEB/DOM4-ja.html#interface-element>`_)\
において、各要素のid属性は\
:code:`DOMString`\ 型であり、これによって要素の\
`unique identifier(ID) <http://www.w3.org/TR/dom#concept-id>`_\
(`一意的な識別子
<http://www.hcn.zaq.ne.jp/___/WEB/DOM4-ja.html#concept-id>`_)\
を持つことができると記されています。

:code:`DOMString`\ はWebIDL [WebIDLJ]_\ の定義によることが\
`9 Historical/9.2 DOM Core
<http://www.w3.org/TR/dom#dom-core>`_\ 節で示されています\
(`8 歴史(変更点)/8.2 DOM Core
<http://www.hcn.zaq.ne.jp/___/WEB/DOM4-ja.html#dom-core>`_)。

`3.10.15 DOMString
<http://www.w3.org/TR/WebIDL/#idl-DOMString>`_ 節で\ :code:`DOMString`\ は
符号単位(code unit)の直列であることが示されています(`3.10.15. DOMString(邦訳)
<http://www.hcn.zaq.ne.jp/___/WEB/WebIDL-ja.html#idl-DOMString>`_)。

`code unit <http://www.w3.org/TR/WebIDL/#dfn-code-unit>`_\ も同書で定義され、
16ビット符号なし整数であり、またUTF-16符号化法と対応付けるとされています\
(`符号単位
<http://www.hcn.zaq.ne.jp/___/WEB/WebIDL-ja.html#dfn-code-unit>`_)。

以上のことから、HTMLにおける要素の識別子にUnicodeの文字を使うことができ、\
内部ではUTF-16の扱いになることがわかります。ただしCSS3では数字・\
ハイフン二つ・ハイフンと数字のいずれかを先頭にはできません。次の節を\
ごらんください。

DOM3においては\ :code:`DOMString`\ がDOM3CORE [DOM3COREJ]_\
で定義されています。\
`1.2.1 The DOMString Type
<http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-C74D1578>`_\
節を参照ください。

CSSにおける識別子
.................
CSSは現在level 3が議論されています。その安定性はCSS2.1の区分により\
モジュール単位で異なるものになっています。この件については\
CSS Snapshot 2010 [CSSSnapshotJ]_\ の\
`1.1 Introduction <http://www.w3.org/TR/css-2010/#intro>`_\
節をお読みください(`1.1 はじめに
<http://standards.mitsue.co.jp/resources/w3c/TR/css-2010/#intro>`_)。

CSS2.1 [CSS21J]_ [CSS22J]_ においては\ `4.1.3 Characters and case
<http://www.w3.org/TR/CSS21/syndata.html#characters>`_ 節で識別子に
どの文字が使えるかを説明しています。第二段落に次の記述があります(\
`4.1.3 文字と活字ケース
<http://momdo.s35.xrea.com/web-html-test/spec/CSS21/syndata.html#characters>`_):
  
  CSSでは、（要素名、クラス、およびセレクタ内のIDを含む）識別子は、\
  文字[a-zA-Z0-9]およびISO 10646でU+00A0以上の文字、またハイフン（-）\
  およびアンダースコア（_）のみを含むことができる。識別子は、数字、\
  2つのハイフン、ハイフンの直後の数字で開始できない。また、識別子は、\
  エスケープされた文字および数字コードとして任意のISO 10646文字を含め\
  ることができる…(後略)

従って、識別子に非ASCII文字を使えます。そのすぐ下にISO 10646はUnicodeと\
文字符号が一対一で対応する旨も記されています。CSS3でもこれを覆す記述は\
見当たらず、CSS2.1の定義を踏襲していると思われます。

JavaScript/ECMAScriptにおける識別子
...................................
ECMAScript [ECMAScriptJ]_\ は大雑把にいうとJavaScriptの標準仕様です。

ECMAScriptの仕様では、\ `7.6 Identifier Names
and Identifiers <http://www.ecma-international.org/ecma-262/5.1/#sec-7.6>`_
節が識別子に使える文字を定義しています(
`7.6 識別子名と識別子
<http://www.webzoit.net/hp/it/internet/homepage/script/ecmascript/ecma262_51/contents/7/7_6/>`_\
)。そこでは明瞭にUnicodeの文字が\
利用可能とされています。一見いくつかの文字種は使えないように思えますが、
Unicode escape sequenceによって最終的にすべての文字が使えるという定義の\
ようです。

関連する拡張やテーマ
--------------------
- `sphinx_html5_basic_theme <https://pypi.python.org/pypi/sphinx_html5_basic_theme>`_

著者
----
鈴見咲 君高(Suzumizaki-Kimitaka), 2011-2015

履歴
----
2.0.5(2015-07-04):

  - 用語集_\ 拡張から抜き出し、同拡張とともにPyPIに登録しました。
  - PyPI 上での公開をはじめました。

2013-12-07:

  Sphinx に合わせて Python 3 で動作するようにしました。

2013-12-06:

  Sphinx 1.2 に適合するように更新しました。

2011-05-24:

  初公開版。\ 用語集_\ 拡張の一部でした。

.. _用語集: https://pypi.python.org/pypi/yogosyu

参考文献
--------
.. [HTML401J] `HTML 4.01 <http://www.w3.org/TR/html401/>`_, \
    `1999年12月24日付勧告 <http://www.w3.org/TR/1999/REC-html401-19991224/>`_ \
    / `HTML 4仕様書邦訳計画 補完委員会邦訳 <http://www.asahi-net.or.jp/~sd5a-ucd/rec-html401j/>`_

.. [HTML5J] `HTML 5 <http://www.w3.org/TR/html5/>`_, \
    `2014年10月28日付勧告 <http://www.w3.org/TR/2014/REC-html5-20141028/>`_ \
    / `もんど氏一部邦訳 <http://momdo.github.io/html5/Overview.html>`_

.. [HTML51J] `HTML 5.1 <http://www.w3.org/TR/html51/>`_, \
    `2015年5月6日付作業草案 <http://www.w3.org/TR/2015/WD-html51-20150506/>`_ \
    / `もんど氏一部邦訳 <http://momdo.github.io/html51/Overview.html>`_

.. [W3CURLJ] `W3C URL <http://www.w3.org/TR/url/>`_, \
  `2014年12月9日付作業草案 <http://www.w3.org/TR/2014/WD-url-1-20141209/>`_

.. [WHATWGURLJ] `WHATWG URL Living Standard 2015年5月9日版 <https://url.spec.whatwg.org/>`_
  / `広瀬行夫氏邦訳 <http://www.hcn.zaq.ne.jp/___/WEB/URL-ja.html>`_

.. [DOM4J] `W3C DOM 4 <http://www.w3.org/TR/dom/>`_, \
    `2015年4月28日付最終作業草案 <http://www.w3.org/TR/2015/WD-dom-20150428/>`_ \
    / `広瀬行夫氏邦訳 <http://www.hcn.zaq.ne.jp/___/WEB/DOM4-ja.html>`_

.. [WebIDLJ] `WebIDL <http://www.w3.org/TR/WebIDL/>`_, \
    `2012年4月19日付勧告候補 <http://www.w3.org/TR/2012/CR-WebIDL-20120419/>`_ \
    / `広瀬行夫氏邦訳 <http://www.hcn.zaq.ne.jp/___/WEB/WebIDL-ja.html>`_

.. [DOM3COREJ] `DOM Level 3 Core <http://www.w3.org/TR/DOM-Level-3-Core/>`_, \
    `2004年4月7日付勧告 <http://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/>`_

.. [CSSSnapshotJ] `CSS Snapshot 2010 <http://www.w3.org/TR/css-2010/>`_, \
    `2011年5月12日付 <http://www.w3.org/TR/2011/NOTE-css-2010-20110512/>`_ \
    / `矢倉眞隆氏邦訳 <http://standards.mitsue.co.jp/resources/w3c/TR/css-2010/>`_

.. [CSS21J] `CSS 2.1 <http://www.w3.org/TR/CSS2/>`_, \
    `2011年6月7日付勧告 <http://www.w3.org/TR/2011/REC-CSS2-20110607/>`_ \
    / `もんど氏邦訳 <http://momdo.s35.xrea.com/web-html-test/spec/CSS21/cover.html>`_

.. [CSS22J] `CSS 2.2 <http://dev.w3.org/csswg/css2/>`_, \
    2015年5月28日個別版としてはリンク切れ \
    / `もんど氏邦訳 <http://momdo.github.io/css2/cover.html>`_

.. [ECMAScriptJ] `ECMAScript 5.1 <http://www.ecma-international.org/ecma-262/5.1/>`_, 2011年6月発行 \
  / `webzoit氏(?)邦訳 <http://www.webzoit.net/hp/it/internet/homepage/script/ecmascript/ecma262_51/>`_
