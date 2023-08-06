Introduction
============


Normalize Katakana to Hiragana for ZCTextIndex.
When you do "quick install", the setting of Plone instance will change from default Normalizer (I18NNormalizer) to this normalizer (KanaNormalizer)
And, You shuld do "ReIndex" manually.


Japanese informaiton.
------------------------------

アドンの適用("quick install")が必要です。その後、ZMIから手動で "ReIndex"を行ってください。

検索インデックス(ZCTextIndex) のノーマライズ機能で、カタカナをひらがな置換えます。検索時、ひらがなとカタカナを同一視します。
副作用として、ひらがな・カタカナ混じりの文字をミスヒットする可能性があります。
(例: 「アクセスして」を「あくせすして」としますので、「すし」というキーワードに検索ヒットしてしまいます)

