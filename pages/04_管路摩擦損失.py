import streamlit as st

# 網頁標題與基本訊息
st.title("實驗四：黏滯係數量測")
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("**組員：** 呂昕叡, 李茂廷, 林承志, 姜陳昊")
st.markdown("**日期：** 113年10月24號")

# 壹、實驗目的
st.header("壹、實驗目的")
st.write("量測液體黏滯係數，實驗中改變液體溫度，紀錄黏滯係數與溫度變化的關係")

# 貳、儀器與設備
st.header("貳、儀器與設備")
st.image("./imges/a.jpg", caption=" ")
st.image("./imges/b.jpg", caption=" ")
st.image("./imges/c.jpg", caption=" ")

st.write("""
1. 黏度計: Brookfield DV-E 可程式黏度計，具備轉速、溫度感應等功能
2. 電表
3. 轉針
4. 燒杯
5. 電表量溫度專用線
""")

# 參、實驗原理
st.header("參、實驗原理")
st.write("DV-E 的操作原理是透過旋轉浸入測試流體中的轉子來進行測量。流體對轉子的黏滯阻力會導致校準彈簧發生偏轉，該偏轉通過旋轉式傳感器進行測量，並產生扭矩信號。DV-E 的測量範圍（以厘泊或毫帕·秒為單位）取決於轉子的旋轉速度、轉子的大小與形狀、轉子旋轉所使用的容器以及校準彈簧的滿量程扭矩。")
st.write("黏滯係數分為兩種，一為絕對黏度(Absolute Viscosity)，單位為 P(poise)，1 P = 1 (g/cm)s = 100 cP；一為動力黏度(Kinematic Viscosity)，單位為 St(stoke)，1 St = 1 cm2/s = 100 cSt。又絕對黏度與動力黏度之關係為下式")
st.write("centiPoises (cP) = centiStokes (cSt) x Density(g/cm3)	(3)")
st.image("./imges/d.png", caption=" ")
st.image("./imges/e.png", caption=" ")
st.image("./imges/f.png", caption=" ")
st.image("./imges/g.png", caption=" ")
st.header("黏滯力之物理意義")
st.write("氣體:氣體之黏滯力是由氣體分子之間碰撞，造成動量交換而產生")
st.image("./imges/h.png", caption=" ")
st.write("黏滯力與溫度之關係： 當溫度增加，氣體分子之能量與動量均增加，分子間之碰撞及動量交換亦增加，故黏滯力增加。對於液體，分子鍊間之凝聚力隨溫度增加而破壞，黏滯力亦減小。當馬達旋轉帶動轉子(Rotor)同步旋轉，轉子表面與液體間產生相對摩擦力，藉由簡單的換算公式，轉換成讀取之數據(黏度值)。馬達與轉子之間最重要的介質，是一條經過校正的精密游絲。當液體黏度大於游絲彈性時，會帶動指針於刻度盤上產生一個偏角，即可得知樣本的絕對黏度。")

st.write("黏滯力與溫度之間的關係：當溫度上升，黏滯力會隨之減少")
# 若有更多公式或數據表，可以插入 st.latex 或 st.dataframe 來呈現

# 肆、實驗步驟
st.header("肆、實驗步驟")
st.write("1.先將黏度計安裝完成並調整水平調整使水瓶氣泡至於黑圈中且打開黏度計電源")
st.image("./imges/i.jpg", caption=" ")
st.write("2. 取一個 600ml 標準燒杯，將樣品加至轉針測量高度，黏度計準備好參數設定完成，將護架裝置上去")
st.image("./imges/j.jpg", caption=" ")
st.write("3.將黏度計放置於測量樣品中，裝上轉針")
st.image("./imges/k.jpg", caption=" ")
st.write("4.設定轉針號碼與轉速並打開馬達開關鈕測量樣品黏度。帶黏度穩定後，讀取顯示幕數據並記錄，再依序對 40℃、60℃、70℃進行量測。")
st.image("./imges/l.png", caption=" ")
st.write("(三圖)依序為 43℃、61℃、78℃")
st.write("5.查看黏度計數據")
st.image("./imges/m.png", caption=" ")
st.image("./imges/n.png", caption=" ")
st.image("./imges/o.png", caption=" ")
st.image("./imges/p.png", caption=" ")
st.write("(有上傳yt的六秒錄影)")
st.write("https://youtube.com/shorts/Yx-8dL7XaOs?feature=share")
st.write("(一)轉針號碼設定說明")
st.write("調整轉針設定轉針號碼(例:由 1 號變換至 3 號針)。")
st.image("./imges/q.jpg", caption=" ")
st.write("(二)轉速設定說明")
st.write("選擇轉子換轉速組合，使扭矩百分比讀值在 10-100%範圍內。黏度大的樣品，使用面積小的轉子換較低的轉速，對於低黏度的樣品，情況相反")
st.image("./imges/r.jpg", caption=" ")
# 伍、實驗結果與討論
st.header("伍、實驗結果與討論")
st.write("水的溫度越高時，黏滯係數就越小，表示液體在高溫中，流動性越好，在低溫時流動性較差")
st.write("在不同轉速下，黏滯係數變化不大。")
st.write("因為低黏滯係數在轉子表面與液面產生相對摩擦力在轉速不同，相差不大，所得到的絕對黏度也較相近。")
st.write("4.請描述本次實驗心得及在學習上或未來工作上可以應用之(設計)案例?")
st.write("在這次的實驗中，我們主要測量了流體的黏滯係數，藉此了解流體在管道或其它介質中的運動特性。黏滯係數是描述流體內部阻力的一個重要參數，它對日常生活中的許多應用，如液壓系統、潤滑油和藥物輸送等，都有直接影響。並記錄在不同溫度下的流速變化，以驗證黏滯係數是否隨溫度變化而改變。在實驗中，我們發現環境溫度對結果有很大的影響，因為溫度越高，液體流動越快，黏滯係數也相對較小。")
st.write("醫療設備與生物工程: 在醫療器械設計中，如血液流動設備（如人工心臟、血管支架）或藥物輸送系統，流體的黏滯性是設計的重要考量因素。血液的黏滯係數對醫療設備的設計至關重要，因為需要精確控制流體流動，以避免不必要的壓力或阻塞。")
st.write("航太與能源產業: 航太工程中的燃料系統、冷卻劑輸送系統都需要對黏滯係數有深入理解。黏滯係數的影響不僅限於設計中流體的選擇，還包括在極端條件下如高溫或低壓下流體性能的變化。這對火箭或衛星的推進劑設計也有著關鍵影響。")

# 參考文獻
st.header("參考文獻")
st.write("""
1. http://www.chuanhua.com.tw/ch-web/pdf/new/toki_b2-type.pdf
2. http://www.wunan.com.tw/www2/download/...
3. 國立東華大學 黏滯係數測定實驗
""")

