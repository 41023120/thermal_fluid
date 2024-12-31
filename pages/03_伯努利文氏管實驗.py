import streamlit as st

st.title("實驗三: 伯努利文氏管實驗")
st.image("./imges/3.1.png", caption=" ")



# 在這裡添加實驗一的具體內容，如圖表、數據等
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("### 113學年度『機械工程實驗(二)：熱流力實驗』")
st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("""**組員：** 
            41023120 呂昕叡
            41023124 李茂廷
            41023131 林承志
            41023142 姜陳昊
""")
st.markdown("**日期：** 113年12月24號")
# 壹、實驗目的
st.header("壹、實驗目的")
st.write("""這裡流體力學中，伯努利定理描述流體沿著一條穩定、非粘滯性，不可壓縮的流線移動，其壓力、速度及高度的變化形成一關係式，
         此一關係式對於流體力學中許多運動的特性做了合理的解釋，例如：棒球的運動軌跡，飛機機翼的升力等。
         藉由此實驗來檢驗伯努利方程式中能量守恆的概念，如此對於流體運動中速度與壓力的關係能有較深刻的認識。""")
st.write(""" 本標準型流量產生裝置，係依據 AMCA210-16 規範之標準所建立，此AMCA210-16 規範為工業界所採用之標準風量量測單元，而本設備之核心架構就是以此一基礎上所建立之標準風量產生器。""")
st.write("""體力學中，伯努利方程式描述流體沿著一條穩定、非粘滯性及不可壓縮的流線移動，其壓力、速度及高度的變化形成一關係式，此一關係式對於流體力學中許多運動的特性做了合理的解釋，例如：棒球的運動軌跡，飛機機翼的昇力等。而本裝置的目的為幫助致力於流體力學學習的學員，藉由文氏管的壓力與速
度的量測，來檢驗伯努利方程式能量守恆與質量守恆的概念，如此對流體運動中速度與壓力的關係有較深刻的認識與了解。另外，本裝置所使用的標準風量產生裝置，係根據國際規範 AMCA 210-16 製造而得，其精確度的可在 3 % 以內，其結構及流量計算原理與目前廣泛應用於工業界風扇及系統阻抗測試之 AMCA 風
洞是一致的，而學員透過實際量測，可對風洞流量量測的原理與方法做深入的了解。
 """)
st.write("""因此，學習者若能活用部份流體及熱傳遞學裡的知識，並且按部就班學習、測試及體會，同時這個架構是 IT 產業界在研發及實際生產中正在使用的工業技術，將使學習者產學的認知關係更加密切，必能裨益不少。 """)

st.write(""" """)
# 貳、儀器與設備
st.header("貳、儀器與設備")
st.image("./imges/3.2.png", caption=" ")
st.image("./imges/3.3.png", caption=" ")
st.image("./imges/3.4.png", caption=" ")
st.image("./imges/3.5.png", caption=" ")
st.image("./imges/3.6.png", caption=" ")
st.image("./imges/3.7.png", caption=" ")
st.image("./imges/3.8.png", caption=" ")
st.image("./imges/3.27.png", caption=" ")

# 參、實驗原理
st.header("參、實驗原理")
st.write("標準風量產生裝置結構及原理")
st.write("AMCA (Air Movement and Control Association)風量計算原理")
st.write("""AMCA-210 為美國空氣移動控制協會訂立之標準，符合美國國家標準。 本項標準風量產生裝置的所有外觀、尺寸及量測硬體，均依據美國空氣移控協 會標準 AMCA 210-16 規範的 Fig. 15 結構設計製造，規範中規定了風洞腔體相關尺寸、量測點位置、整流網（settling means）配置原則等。 """)
st.image("./imges/3.9.png", caption=" ")

st.write("""  其中，對於關鍵元件─噴嘴(Nozzle)的設計，也有其依據的準則，其尺寸、表面粗糙度都受到規範的限制。噴嘴為一特殊設計的漸縮管，具有較高且穩定的 Cd值，在不同的雷諾數狀態下，可達 0.95 ~ 0.99，表示流體通過時會有較小的摩擦損失，可有效用做流量計算。""")
st.image("./imges/3.28.png", caption=" ")
st.image("./imges/3.10.png", caption=" ")
st.image("./imges/3.11.png", caption=" ")
# 肆、實驗步驟
st.header("肆、實驗步驟")
st.write("1. 開啟控制面板上的 1.1 System Power：")
st.image("./imges/3.12.png", caption=" ")
st.write("2. 確認乾溼求溫度計的濕球水箱有水。")
st.image("./imges/3.13.png", caption=" ")
st.write("3. 系統開機後需暖機 10 分鐘後方可開始測試。紀錄乾溼球溫度及大氣壓力。")
st.image("./imges/3.14.png", caption=" ")
st.write("4. 確認輔助風機頻率調整旋鈕旋鈕逆時針旋轉至底輔助風機頻率顯示器：顯示目前輔助風機運轉頻率值 0.0 Hz。")
st.image("./imges/3.15.png", caption=" ")
st.write(""" 5. 根據所需實驗的風量選擇合適的噴嘴後，於標準流量產生器安裝噴嘴，噴嘴安裝方式可參考 3.2 標準風量產生裝置操作。注意，安裝噴嘴時請勿使噴嘴受碰撞，須小心安裝，以免造成噴嘴表面刮傷。""")
st.image("./imges/3.16.png", caption=" ")
st.write("6. 按下面板 RUN 按鍵，使變頻器與風機產生連動關係。調整變頻器旋鈕，使 P56 顯示為一定值，如：35 mmAq。。")
st.image("./imges/3.17.png", caption=" ")
st.write("7.記錄其他溫度、壓力的參數數值。")
st.image("./imges/3.18.png", caption=" ")
st.image("./imges/3.19.png", caption=" ")
st.image("./imges/3.20.png", caption=" ")
st.image("./imges/3.21.png", caption=" ")
st.image("./imges/3.22.png", caption=" ")
st.image("./imges/3.23.png", caption=" ")
# 伍、實驗結果與討論
st.header("伍、實驗結果與討論")
st.image("./imges/3.24.png", caption=" ")
st.image("./imges/3.25.png", caption=" ")
st.image("./imges/3.26.png", caption=" ")


# 參考文獻
st.header("參考文獻")
st.write("""
1. 20191018-9341 伯努利理論實驗裝置 使用手冊_8945-1 虎科大
""")

