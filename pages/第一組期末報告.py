import streamlit as st

st.title("期末報告")
# 在這裡添加實驗一的具體內容，如圖表、數據等
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("### 113學年度『機械工程實驗(二)：熱流力實驗』")
st.markdown("期末報告")
st.markdown(" 一、創新夾持裝置機械設計")
st.markdown(" 二、環境量測與控制裝置機械設計")
st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("""**組員：** 
            41023120 呂昕叡
            41023124 李茂廷
            41023131 林承志
            41023142 姜陳昊
""")
st.markdown("**日期：** 113年12月31號")
# 壹、實驗目的
st.header("一、	概論")
st.write("主題一、創新夾持裝置機械設計")
st.write(" 1. 真空產生器的特點 ")
st.write(""" 
         ●	單段真空產生器：低成本、輕便小巧
         ●	超靜音真空產生器：高效率、超靜音、可靠度高、堅固耐用
""")
st.write(" 2. 真空產生器的產品與功能介紹")
st.write(""" ●單段真空產生器：EV單段式真空產生器，提供了一個低成本、輕便小巧的真空產生器，
         二件式的設計可選配直通式的消音器使吸入的雜物可以從排出口排出，直通式消音器是一種無堵塞的設計，被吸入的雜物會經過真空的通道由消音器排出。
         本體結構是以鋁合金NC加工製作後做黑色陽級處理，噴嘴以鍍電解鎳的提高表面硬度的處理，本系列的規格依噴嘴直徑0.5mm，1.0mm，1.5mm，2.0mm四種規格。""")
st.image("./imges/9.1.png", caption="單段真空產生器 ")
st.write(""" ●超靜音真空產生器：本體鋁合金底座,銅合金的噴管以NC加工製作,產品可靠度高,堅固耐用，多段式、高效率雙噴管抽氣設計，低壓力（3.5Bar）作動，空氣消耗量最小、真空度高（-660mmHg）、 
  真空抽氣量大，抽氣性能較一般產生器大約2倍，氣壓控制閥＋真空破壞閥＋真空過濾器＋真空檢知開關多機能一體結構，亦可分別選項組合，1/8"及1/2"堅固的鋁合金配管底座可供選擇。
  
""")
st.image("./imges/9.2.png", caption="1/2配管座 ")
st.image("./imges/9.3.png", caption=" 1/8配管座")


st.write("主題二、環境量測與控制裝置機械設計")
st.write("1.散熱器元件或模組的特點與功能介紹 ")
st.write("散熱片，以導熱性佳、質輕、易加工之金屬，貼附於發熱表面，以複合的熱交換模式來散熱。 ")
st.write("散熱片不需要額外的驅動能源就能執行散熱，是最典型的被動性散熱元件。 ")
st.write(""" 每種散熱片材質材料其導熱性能是不同的，按導熱性能從高到低排列，分別是銀，銅，鋁，鋼，不過如果用銀來作散熱片會太昂貴，最好的方案為採用銅質。
         雖然鋁便宜得多，但顯然導熱性就不如銅好（大約只有銅的百分之五十多點）。
         常用的散熱片材質是銅和鋁合金，二者各有其優缺點。
""")
st.write("銅的導熱性好，但價格較貴，加工難度較高，重量過大，熱容量較小，而且容易氧化。 ")
st.write(""" 
純鋁太軟，不能直接使用，都是使用的鋁合金才能提供足夠的硬度。
鋁合金的優點是價格低廉，重量輕，但導熱性比銅就要差很多。
有些散熱器就各取所長，在鋁合金散熱器底座上嵌入一片銅板。

""")
st.image("./imges/9.4.png", caption=" ")
st.header("二、	原理與設計方法(機械設計與繪圖)")
st.write("主題一、創新夾持裝置機械設計")
st.write(" 1.真空產生器設計與要求規範")
st.write("鋁塊大小76x53x26mm，管路連接口D=3。")
st.write("  2.真空產生器設計方法")
st.image("./imges/9.5.png", caption=" ")
st.image("./imges/9.6.png", caption=" ")
st.image("./imges/9.7.png", caption=" ")
st.write("  3.依據原理與工件大小之零組件設計圖")
st.image("./imges/9.8.png", caption="接頭規格 ")
st.image("./imges/9.9.png", caption=" 工程2D工程圖 ")
st.image("./imges/9.10.png", caption="工件3D前視圖 ")
st.image("./imges/9.11.png", caption=" 工件3D等角視圖")
st.image("./imges/9.12.png", caption="實體圖1")
st.image("./imges/9.13.png", caption="實體圖2")
st.write("主題二、環境量測與控制裝置機械設計")
st.write("散熱片是通過熱的傳導方式進行散熱片，熱傳導方式有：傳導、對流、輻射。")
st.write(""" 輻射：指熱能從熱源以電磁的形式(由光子傳送)直接發散出去。
         輻射可以在真空中進行。輻射的傳熱效能取決於熱源的材料以及表面的顏色。""")
st.write(""" 傳導：指分子之間的動能交換，能量較低的粒子和能量較高的粒子碰撞
         從而獲得能量(是透過物理的直接接觸)，單獨的一塊散熱片是不能實現熱能的傳導的，傳導是散熱片從CPU獲得熱量的最主要途徑。""")
st.write(""" 對流：指透過熱的物質的運動來實現熱的傳遞。這意味着，熱能是來自於被氣體或者液體所包圍熱源，透過分子的移動來實現熱能的傳遞的。
         我們可以採用在散熱片上添加風扇的方法來實現強制對流。""")
st.image("./imges/9.14.png", caption="2D設計圖")
st.image("./imges/9.15.png", caption="3D圖")


st.header("三、	實驗量測與數據分析")
st.write("主題一、創新夾持裝置機械設計")
st.write("1.	實驗測量數據")
st.image("./imges/9.16.png", caption="數據表")
st.write("2.列出軟體分析過程")
st.write("(1)選擇模態")
st.image("./imges/9.17.png", caption=" ")
st.write("(2)匯入圖檔")
st.image("./imges/9.18.png", caption=" ")
st.write("(3)設置MESH")
st.image("./imges/9.19.png", caption=" ")
st.write("(4)設置入口inlet")
st.image("./imges/9.20.png", caption=" ")
st.write("(5)設置出口outlet")
st.image("./imges/9.21.png", caption=" ")
st.write("(6)設置牆壁")
st.image("./imges/9.22.png", caption=" ")
st.write("(7)設置環境wall")
st.image("./imges/9.23.png", caption=" ")
st.write("(8)設置邊界條件")
st.image("./imges/9.24.png", caption=" ")
st.write("(9)進行最佳化設置、計算設置")
st.image("./imges/9.25.png", caption=" ")
st.write(" (10)結果分析")
st.image("./imges/9.26.png", caption="流線-選擇壓力")
st.image("./imges/9.27.png", caption="壓力圖分析結果")


st.write("主題二、環境量測與控制裝置機械設計")
st.write("1.	實驗測量數據")
st.image("./imges/9.28.png", caption="數據表")
st.write("2.	分析步驟與過程")
st.write("(1)	導入零件(import>Browse)")
st.image("./imges/9.29.png", caption=" ")
st.write("(2)	加入Steady-State Thermal(穩態熱)")
st.image("./imges/9.30.png", caption=" ")
st.write("(3)	設定材料性質 Engineering Data")
st.image("./imges/9.31.png", caption="	Structural Steel > Engineering Data Sources ")
st.image("./imges/9.32.png", caption=" 	General Materials > 加入Alumium Alloy")
st.image("./imges/9.33.png", caption=" ")
st.write("(4)	加入材料")
st.image("./imges/9.34.png", caption=" ")
st.write("(5)	設定網格條件")
st.image("./imges/9.35.png", caption=" ")
st.write("(6)	給予底部5W的熱")
st.image("./imges/9.36.png", caption=" ")
st.write("(7)	設定周圍四個面為絕熱的條件")
st.image("./imges/9.37.png", caption=" ")
st.write("(8)	設定散熱區域")
st.image("./imges/9.38.png", caption=" ")
st.write("(9)	選擇要分析的數據")
st.image("./imges/9.39.png", caption=" ")
st.write(" (10)結果分析")
st.image("./imges/9.40.png", caption="溫度分布圖")

st.write("主題三、bladeless wind turbine結構設計僅Fluent模擬")
st.image("./imges/x1.png", caption=" ")
st.image("./imges/x2.png", caption=" ")
st.image("./imges/x3.png", caption=" ")
st.image("./imges/x4.png", caption=" ")
st.video("./imges/0.1.mp4")
# 肆、實驗步驟
st.header("四、	結果與討論")
st.image("./imges/s2.png", caption=" 評分表")
st.write("主題一、創新夾持裝置機械設計")
st.image("./imges/s3.png", caption=" ")
st.image("./imges/s4.png", caption=" ")
st.image("./imges/s5.png", caption=" ")
st.image("./imges/s6.png", caption=" ")

st.write("""
電腦模擬出來和實際測量差距極大，我們認為因為圖和實際加工出來有稍微尺寸上的公差，還有鑽頭在鑽時的鑽唇沒有考慮進去，在結果出來誤差數據相當的大，
         所以在實驗前應該將這些變數也考慮進去，在設計時也須注意這些細節。
""")
st.video("./imges/2.MOV")
st.write("主題二、環境量測與控制裝置機械設計")

st.image("./imges/s7.png", caption=" ")
st.image("./imges/x5.png", caption=" ")

st.write("""
電腦模擬所產生的數據與實際測量結果之間，往往會因為外界因素的影響而產生誤差。
例如，當天考試時，環境中的濕氣變化、散熱片的狀態是否良好（如是否生鏽或損壞）等，都會直接影響實際測量的數據。而電腦模擬的數據則是在理想化條件下進行計算，假設不存在外界因素的干擾，並且假定系統運行完美無缺。
因此，模擬結果通常無法完全反映現實中的複雜變數，這也是為何在實驗中會發現數據與模擬結果存在誤差的原因。這一點提醒我們，在進行實驗或設計時，必須考慮現實環境中的變數，以便更加準確地理解和解釋數據的差異。
""")

# 伍、實驗結果與討論
st.header(" 結論")
st.write("主題一、創新夾持裝置機械設計")
st.write("""
經過這次的課程，我們在老師的指導下深入了解了真空原理，並通過老師所提供的示範，親自動手設計尺寸並製作實體模型，並運用程式模擬進行比對。在進行實驗後，我們發現實驗結果與模擬數據之間的誤差相當大，這使得我們開始反思並深入思考為何會產生如此大的差異。
在組員討論後，我們認為誤差值偏大的原因可能來自於繪圖過程中未能注意到加工時所使用鑽頭前端的鑽唇形狀，以及在加工過程中產生的公差。這些微小的尺寸誤差，在實際操作中未能充分考慮，最終導致了我們的測量結果與模擬數據之間的顯著差異。這次經歷讓我們深刻體會到細節在設計和加工過程中的重要性。

""")
st.write("主題二、環境量測與控制裝置機械設計")
st.write("""
在此次實驗中，我們首次進行溫度測量時發現，散熱頂部的溫度竟然高於底部溫度，且與模擬數據相比，結果差異極大。經過組員討論並聽取老師的指導，我們找出了問題的根源：實驗時應該要兩個量測溫度器譯起測量，才能提供正確的數值，如果不一起測量則，無法達到預期的散熱效果。

""")
st.image("./imges/s8.png", caption=" ")





