Title: Dr. Chua Ming Yam: 練習が鍵となります。
Date: 2018-09-7 12:00
Author: Ai Sin Chan
Tags: インタビュー; エンジニア; 2018; chua ming yam; airplanes; リモートセンシング; surveillance; 
Lang: en
Thumbnail: images/drchuamingyam.jpg
Slug: interview-with-dr-chua-ming-yam
Summary: 現在千葉大学教授を務める、Dr. Chua Ming Yamへインタビューしました。

Chua Ming Yam博士と、博士のソフトウェア開発の経験とプロジェクトに関するチャットをしました。
彼は講師や研究者としての仕事に加えて、フリーランス相談を行っています。
現在、千葉大学助教授を務めており、リモートセンシングや監視の目的でBoeing 737などの商用飛行機に搭載可能なレーダーの構築を専門としております。
博士は、過去の好きな時の1つとして料理をあげます。博士の技術的な仕事は 博士の[ウェブサイト](https://chuamingyam.wordpress.com/)で確認できます。

![Dr. Chua Ming Yam]({filename}/images/drchuamingyam.jpg)

**あなたが使った最初のコンピュータは何でしたか？それはいつですか？**

> 小学校の時に、初めてコンピュータを使いました。そのコンピューターは、インテル80486DXプロセッサ（2MB RAM搭載）で動作し、
アクセサリには外部プラグインCD-ROM が2つ、グラフィックスカードVGA 640x480、外部プラグインサウンドカードが付属していました。
OSはGUI（グラフィックユーザーインターフェイス）なしのコマンドプロンプト上の、Windows 3.1でした。
ワープロソフトは、Word PerfectとLotus 123でした。その時は、モデムもインターネットもありませんでした。
私の父が、ロータス123を学ぶために買ったのですが、使っていないときに、私や兄弟が使っていました。
私は趣味で、DOSバッチスクリプティングを実行するために使っていましたが、これがコンピューティングへの関心を呼び起こしました。

**実生活に使われた、最初のプログラムは、何ですか？**

> 中学校で、校内の教師生徒の共同で運営されていた文具店で、スプレッドシートスクリプトを作成しました。そうしたことで、コンピュータエンジニアリングを専攻する、という私の野望に拍車がかかりました。大学に入学するときは、代わりに電子工学を選択しました。

**ソフトウェア開発プロジェクトの、何が好きですか？**

> ソフトウェアソリューションを完成したときの、満足感と達成感が好きです。私が作成した独自のもの、それでもって、問題を解決して解決することができます。

**ハードウェア開発はどのようにソフトウェア開発に関係していますか？もしくは逆でも良いのですが？**

> ハードウェアとソフトウェアは不可分であり、手を携えなければなりません。料理のような感じです。例えると、ハードウェアは原材料、ソフトウェアは熱、調味料、水のようなもので、原材料を料理に仕上げます。どちらも重要な役割を果たします。

**どのコーディング言語が専門ですか？**

> 低レベル言語：アセンブリ言語、Verilog HDL

> 高レベル言語：C、Basic、C＃、Matlab

> グラフィカルプログラミング：Labview,、私は、Certified Labview Associate Developer(CLAD)です。

**時と共に、ツールはどのように変わってきたと思いますか？**

> 電子システムの設計を始めた頃は、アセンブリ言語、C言語、およびマイクロコントローラのファームウェアを使用して、マイクロコントローラでソリューションを構築していました。DAU（データ取得ユニット）を含むレーダー受信機の開発に移ったときには、ユーザーの制御と構成のためのGUIを作成するため、マイクロコントローラー、ファームウェア、およびVisual Basicを使用していました。私がレーダーの構築へ進んだ頃は、シミュレーション、アルゴリズム設計、概念証明のためにMatlabを使用していました。FPGAを使ってハードウェアを開発し、LabviewでGUIを開発しました。最近のSAR（合成開口レーダー）コントローラシステムの開発プロジェクトでは、C＃、Labview、FPGA、Verilog HDLを使用しています。レーダーで収集されたデータを処理するのに、Matlabを使用します。

**MYebills のソリューションがもたらす、業界への貢献は？**

> In one of my consultation projects, I developed a power tool test rig comprising 6 test stations for Bosch, the power tool manufacturer. The main purpose of the test rig is to conduct power tool endurance tests. The test rig is to simulate a user operating the power tool and test the tool until the end of its product life.

> The software is capable of collecting data input from sensors, including temperature, torque, reaction torque, and most importantly, the lifetime of the power tool. After data collection, it will then analyze and recognize the symptoms before the power tool breaks down, to provide clues on how to lengthen the lifetime of the power tool.

> In addition, the software solution also included ergonomic analysis for the power tool, such as the duration of use that will trigger the onset of hand-arm vibration syndrome in the user. The data can also be used to analyze vibration injuries, for example neurological, vascular, and musculoskeletal disorders.

> In a separate project on the development of radar controller and processor, I used a combination of commercial hardware and dedicated hardware that cannot be bought which I made by designing FPGA boards. Then I integrated the hardware with software functions and developed a user interface with C#, which is capable of controlling the system and executing high-speed large volume data acquisition.

> Raw data acquired by the radar mounted on an airplane during flight tests was processed using Matlab that runs image formation algorithm to produce radar images. Radar sensors are weatherproof and more superior than optical sensors and can be used for remote sensing application such as disaster damage assessment, land deformation observation, snow monitoring, oceanography, terrain classification, and target detection.

**What are the challenges that you face when delivering software development projects?**

> In R&D projects, we don’t usually have a dedicated software developer, whatever function needed has to be developed by myself, even when it means learning a new language or using a new tool to achieve the objectives.

**What are the most important technical skills that a developer should possess?**

> Code reusability, code optimization, speed, resource utilization, scalability, and expandability. In R&D applications, the software is of a smaller scale as compared to commercial applications, system architecture design is not given as much emphasis, and programming skill not as specialized.

**What are the soft skills that are crucial for a developer?**

> Project management and time management, managing the project timeline and deadlines. Sometimes the project requires dealing with third-party supplier or collaboration between different teams, communication is important.

**Are the fresh graduates today equipped with the right skills with their tertiary education?**

> The training that an undergraduate receives is like being introduced to the recipe, which contains the essential steps. Without practice, the final dish cannot be produced. The best way to learn programming is by practicing, it is something that cannot be learned from books alone.

**What advice would you give a fresh graduate entering the industry as a developer?**

> Learn as much as you can when you are young; when an opportunity arises, treasure it. Constantly upgrade yourself; if you stop learning, you will be left behind.

> Skill is not the most important, attitude is the most important. Persevere and do everything well, then you will achieve your targets.

 
