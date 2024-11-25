import re
import csv

# 輸入數據
input_text = """
1.
C. L. Lin, Z. T. Sun and Y. Y. Chen , “Air-mattress system for ballistocardiogram-based heart rate and breathing rate estimation ,” Heliyon , vol. 1, no. 9, 12 2022. (SCI)
2.
Y. Zhang, W. Chen, C. L. Lin, Z. Pei, J. Chen and D. Wang , “Synchronous analyses between electroencephalogram and surface electromyogram based on motor imagery and motor execution ,” Review of Scientific Instruments , 11 2022. (SCI)
3.
J. J. Kao, C. L. Lin and J. Yang , “Adaptive wireless power transfer system with relay transmission and communication ,” IEEE Transactions on Power Electronics , 10 2022. (SCI)
4.
D. Y. Huang, C. L. Lin and Y. Y. Chen , “Securable networked scheme with face authentication ,” IET Biometrics , 09 2022. (SCI)
5.
C. M. Chang, C. L. Lin, B. Huang and Y. Zhang , “Image based control of smart workout systems ,” Biomedical Signal Processing and Control , 08 2022. (SCI)
6.
C. Y. Chen, C. L. Lin and Y. Y. Chen , “Realization of ideal architecture of IoTs ,” ARRAY , 07 2022. (SCI)
7.
C. L. Lin, J. C. Li, C. L. Chiu, Y. W. Andy Wu and Y. W. Jan , “Gyro-stellar inertial attitude estimation for satellite with high motion rate,” The Aeronautical Journal , 04 2022. (SCI)
8.
B. Huang, W. Chen, C. L. Lin, C. F. Juang and J. Wang , “MLP-BP: A novel framework for cuffless blood pressure measurement ,” Biomedical Signal Processing and Control , 03 2022. (SCI)
9.
B. Huang, W. Chen, C. L. Lin, C. F. Juang, Y. Xing, Y. Wang and J. Wang , “A neonatal dataset and benchmark for non-contact neonatal heart rate monitoring based on spatio-temporal neural networks ,” Engineering Applications of Artificial Intelligence , 11 2021. (SCI)
10.
Y. Zhang, W. Chen, C. L. Lin, Z. Pei, J. Chen and Z. Chen , “Boosting-LDA algorithm with multi-domain feature fusion for motor imagery EEG decoding,” Biomedical Signal Processing and Control , 09 2021. (SCI)
11.
Y. C. Lin, C. L. Lin, S. T. Huang and C. H. Kuo , “Implementation of an autonomous overtaking system based on time to lane crossing estimation and model predictive control,” Electronics , 09 2021. (SCI)
12.
B. Huang, C. L. Lin, W. Chen, C. F. Juang and X. Wu , “A novel one-stage framework for visual pulse rate estimation using deep neural networks,” Biomedical Signal Processing and Control , 08 2021. (SCI)
13.
J. J. Kao, C. L. Lin, Y. C. Liu, C. C. Huang and H. S. Jian , “Adaptive bidirectionally inductive power and data transmission system,” IEEE Transactions on Power Electronics , 07 2021. (SCI)
14.
Z. A. Shen, J. Cheng, C. T. Tang, C. L. Lin and C. F. Juang , “Estimation of machine cutting tool wear,” Journal of the Chinese Institute of Engineers , 05 2021. (SCI)
15.
C. H. Tu, Y. C. Chang, C. L. Lin and V. T. Liu , “Motor driving/braking control scheme with integration of multiple driving components,” Asian Journal of Control , 12 2020. (SCI)
16.
T. H. Chen, C. H. Tu, C. L. Lin and S. P. Hsu , “Advanced stabilizing control for electric scooters ,” Asian Journal of Control , vol. 1, no. 32, pp. 20-31, 10 2020. (SCI)
17.
T. H. Chen, C. H. Tu, C. L. Lin and S. P. Hsu , “Advanced tracking control for electric vehicles ,” Asian Journal of Control , vol. 3, no. 23, 10 2020. (SCI)
18.
S. M. Liu, C. H. Tu, C. L. Lin and V. T. Liu , “Field-oriented driving/braking control for electric vehicles ,” Electronics , vol. 9, no. 9, 09 2020. (SCI)
19.
T. Jennawasin, C. L. Lin and D. Banjerdpongchai , “Parameter-dependent linear matrix inequality approach to robust state estimation of noisy genetic networks,” Computers and Chemical Engineering , no. 136, 03 2020. (SCI)
20.
Changchen Zhao, Weihai Chen, Chun-Liang Lin and Xingming Wu, “Physiological Signal Preserving Video Compression for Remote Photoplethysmography,” IEEE SENSORS JOURNAL , vol. 12, no. 19, pp. 4537-4548, 12 2019. (SCI)
21.
C. J. Fong, C. H. Chu, C. L. Lin and A. da Silva Curiel , “Toward most accurate thermometer in space: FORMOSAT-7/COSMIC-2 constellation ,” IEEE Aerospace and Electronic Systems Magazine , vol. 8, no. 34, pp. 12-20, 08 2019. (SCI)
22.
Y. C. Chen, C. H. Tu and C. L. Lin , “Integrated electromagnetic braking/driving control for electric vehicle using fuzzy inference ,” IET Electric Power Applications , vol. 7, no. 13, pp. 1014-1021, 07 2019. (SCI)
23.
C. Zhao, C. L. Lin, W. Chen, M. K. Chen and J. Wang , “Visual heart rate estimation and negative feedback control for fitness exercise ,” Biomedical Signal Processing and Control , no. 56, 07 2019. (SCI)
24.
J. J. Kao, C. L. Lin, C. C. Huang, and C. H. Huang , “Lighting control via magnetic field communication ,” Inventions , vol. 4, no. 4, 04 2019. (SCI)
25.
S. F. Lin, J. R. Tsai and C. L. Lin , “A plan and its current status for Taiwanese Moon exploration: a lunar orbiter,” Journal of Aeronautics, Astronautics and Aviation, vol. 3, no. 52, pp. 217-228, 03 2019. (SCI)
26.
C. L. Lin, H. C. Hung and J. C. Li , “Active control of regenerative brake for electric vehicles,” Actuators , vol. 4, no. 7, 12 2018. (SCI)
27.
C. L. Lin, M. C. Hsieh and T. H. Chen , “Integrated driving and braking control unit for electric bikes ,” SAE International Journal of Vehicle Dynamics, Stability, and NVH , vol. 3, no. 2, pp. 223-242, 10 2018. (SCI)
28.
B. Huang, W. Chen, X. Wu and C. L. Lin, “High-quality face image generated with conditional boundary equilibrium generative adversarial networks,” Pattern Recognition Letters, no. 111, pp. 72-79, 08 2018. (SCI)
29.
T. Fei, W. Chen, F. Tao and C. L. Lin, “Industrial IoT in 5G environment towards smart manufacturing ,” Journal of Industrial Information Integration, no. 10, pp. 10-19, 06 2018. (SCI)
30.
C. L. Lin, M. Y. Yang, E. P. Chen, Y. C. Chen and Y. C. Yu, “Novel antilock braking control system for electric vehicles,” IET Journal of Engineering, vol. 2, no. 2018, pp. 60-67, 02 2018. (SCI)
31.
C. L. Lin and W. X. Li , “Commentary on recent development of biological computer ,” Journal of Phylogenetics & Evolutionary Biology, vol. 6, no. 33, 02 2018. (SCI)
32.
C. Zhao, W. L. Hwang, C. L. Lin and W. Chen, “Greedy orthogonal matching pursuit for subspace clustering to improve graph connectivity,” Information Sciences, 01 2018.
33.
C. C. Huang, C. L. Lin, J. J. Kao, J. J. Chang and G. J. Sheu, “Parking guidance for wireless charge using GMR sensors,” IEEE Transactions on Vehicular Technology, 01 2018.
34.
C. L. Lin, T. Y. Kuo, and W. X. Li, “Synthesis of control unit for future biocomputer,” Evolutionary Bioinformatics, 01 2017.
35.
M. Daouda, C. L. Lin, C. S. Lee, C. C. Yang and C. A. Chen, “Model predictive control of sensorless hybrid stepper motors in auxiliary adjuster for stereotactic frame fixation,” Mechatronics, 01 2017. (SCI)
36.
C. Zhao, C. L. Lin, W. Chen, M. K. Chen and J. Zhang, “Fast and robust remote photoplethysmography measurement for heart rate recognition,” IEEE Transactions on Biomedical Engineering, 01 2017. (SCI)
37.
C. L. Lin, Y. J. Hu and W. X. Li, “Circuit design for static genetic memory,” IET Journal of Engineering, 01 2017.
38.
Y. J. Hu, C. L. Lin and W. X. Li, “Design of dynamic genetic memory,” IET Systems Biology, 01 2017. (SCI)
39.
Y. Y. Chen, C. L. Lin, Y. C. Lin and C. Zhao, “Alcoholic intake detection using electrocardiogram and photoplethysmogram,” IEEE Transactions on Biomedical Engineering, 01 2017.
40.
Y. Y. Chen, C. L. Lin, Y. C. Lin and C. Zhao, “Non-invasive detection of alcohol concentration based on photoplethysmogram signals,” IET Image Processing, 01 2017. (SCI)
41.
C. L. Lin, M. Y. Yang, E. P. Chen, Y. C. Chen and Y. C. Yu, “Novel antilock braking control system for electric vehicles,” IET Journal of Engineering, 01 2017. (SCI)
42.
C. L. Lin, T. Y. Kuo, N. Charoenkit, “Toward theoretical synthesis of biocomputer,” IET Systems Biology, vol. 1, no. 11, pp. 36-43, 01 2017. (SCI)
43.
P. Suebsaiprom, C. L. Lin and A. Engkaninan, “Undulatory locomotion and effective propulsion for fish-inspired robot,” Control Engineering Practice, no. 58, pp. 66-77, 01 2017. (SCI)
44.
C. C. Huang and C. L. Lin, “Wireless power and bidirectional data transfer scheme for battery charger,” IEEE Transactions on Power Electronics, 01 2017. (SCI)
45.
C. C. Huang, C. L. Lin and Y. K. Wu, “Simultaneous wireless power/Data transfer for electric vehicle charging,” IEEE Transactions on Industrial Electronics, vol. 1, no. 64, pp. 682-690, 01 2017. (SCI)
46.
K. H. Chen and C. L. Lin, “Phone to phone wireless charging solution,” Journal of Technology, vol. 1, no. 32, pp. 97-104, 01 2017.
47.
Y. H. Hsu, Y. Y. Chen, C. L. Lin and C. Zhao, “Analysis of heart rate variability via health care platform,” International Journal of Health Care and Medical Sciences, vol. 12, no. 3, pp. 103-116, 01 2017. (SCI)
48.
C. Zhao, W. L. Hwang, C. L. Lin and W. Chen, “Improved optimization algorithm for proximal point-based dictionary updating methods,” Journal of Electronic Imaging, 01 2016. (SCI)
49.
M. H. Lu, C. C. Huang, C. L. Lin and Y. J. Shen, “Demonstrative DC motor control under power communication network,” International Journal of Sensor Networks and Data Communications, vol. 2, no. 5, 01 2016. (SCI)
50.
Y. P. Lin, C. L. Lin, P. Suebsaiprom and S. L. Hsieh, “Estimating evasive acceleration for ballistic targets using an extended state observer,” IEEE Transactions on Aerospace and Electronic Systems, vol. 1, no. 52, pp. 337-349, 01 2016. (SCI)
51.
C. H. Chuang and C. L. Lin, “Optimal design of robust synthetic biological oscillators,” Current Synthetic and Systems Biology, vol. 1, no. 3, 01 2016.
52.
C. L. Lin, T. Y. Kuo and Y. Y. Chen, “Implementation of a genetic logic circuit: bio-register,” Systems and Synthetic Biology, no. 9, pp. 43-48, 01 2015. (SCI)
53.
Y. J. Tsai, C. S. Lee and C. L. Lin, and C. H. Huang, “Development of flight path planning for multirotor aerial vehicles,” Aerospace, no. 2, pp. 171-188, 01 2015.
54.
P. K. Chen and C. L. Lin, “Synthesis of genetic clock with combinational biologic circuits,” IEEE/ACM Transactions on Computational Biology and Bioinformatics, vol. 5, no. 12, pp. 1206-1212, 01 2015. (SCI)
55.
G. J. Sheu, M. J. Sie, M. T. Wu and C. L. Lin, “On the realization of a multifunctional contactless sensor,” International Journal of Artificial Intelligence and Mechatronics, vol. 4, no. 3, pp. 112-117, 01 2015.
56.
C. L. Lin, W. T. Chang and M. H. Lu, “MAC throughput improvement using adaptive contention window,” Journal of Computer and Communications, no. 3, pp. 1-14, 01 2015. (SCI)
57.
P. Suebsaiprom and C. L. Lin, “Maneuverability modeling and trajectory tracking for fish robot,” Control Engineering Practice, no. 45, pp. 22-36, 01 2015. (SCI)
58.
B.R. Ke, C.L. Lin, H. H. Chien, H.W. Chiu and N. Chen, “A new approach for improving the performance of freight train timetabling of a single-track railway system,” Transportation Planning and Technology, vol. 2, no. 38, pp. 238-264, 01 2015. (SCI)
59.
C. K. Chen, C. L. Lin, S. L. Lin and C. T. Chiang, “Data encryption and transmission based on personal ECG signals,” International Journal of Sensor Networks and Data Communications, vol. 2, no. 4, 01 2015. (SCI)
60.
P. M. Hsu and C. L. Lin, “Robust stability on averaging behavior of linear time-varying uncertain systems,” Systems Science and Control Engineering, 01 2015. (SCI)
61.
C. H. Chuang and C. L. Lin, “Synthesizing genetic sequential logic circuit with clock pulse generator,” BMC Systems Biology, vol. 63, no. 8, 01 2014. (SCI)
62.
M. Y. Yang, M. T. Wu, C. L. Lin, and C. S. Lee, “Design of an Anti-lock Braking System for Electric Vehicles,” IEEE Transactions on Control Systems Technology, 01 2014.
63.
W. C. Lin, C. L. Lin, P. M. Hsu, and M. T. Wu, “Realization of anti-lock braking strategy for electric scooters,” IEEE Transactions on Industrial Electronics, vol. 6, no. 61, pp. 2826-2833, 01 2014. (SCI)
64.
C. H. Yu, C. L. Lin and P. M. Hsu, “A new algorithm to achieve bandwidth fairness: Power-RED,” Journal of Engineering, NCHU, vol. 1, no. 25, pp. 1-7, 01 2014.
65.
C. H. Chuang, C. L. Lin and Y. C. Lin, “Robust optimal control of time-delay systems based on Razumikhin theorem,” Asian Journal of Control, vol. 1, no. 16, pp. 1-8, 01 2014. (SCI)
66.
T. Jennawasin, M. Kawanishi, T. Narikiyo and C. L. Lin, “Robust D-stability analysis via positive polynomials and LMIs,” International Journal of Computational Intelligence in Control, vol. 2, no. 5, pp. 75-82, 01 2013.
67.
S. L. Lin, C. K. Chen, C. L. Lin, W. C. Yang and C. T. Chiang, “Individual identification based on chaotic electrocardiogram signals during muscular exercise,” IET Biometrics, 01 2013. (SCI)
68.
S. L. Hsieh, C. L. Lin and Y. P. Lin, “Trajectory estimation based on extended state observer with filter,” Aeronautical Journal, 01 2013. (SCI)
69.
C. W. Huang, C. L. Lin and Y. P. Lin, “Estimator design for re-entry targets,” ISA Transactions, 01 2013. (SCI)
70.
C. H. Chuang and C. L. Lin, “A novel synthesizing genetic logic circuit: frequency multiplier,” IEEE/ACM Transactions on Computational Biology and Bioinformatics, 01 2013.
71.
C. L. Lin and P. K. Chen, “Synthesizing periodic triggering signals with genetic oscillators,” IET Systems Biology, 01 2013. (SCI)
72.
M. T. Wu, C. L. Lin, C. C. Lin and L. P. Chung, “Stabilizing current driver for high-voltage light-emitting diodes,” IET Power Electronics, 01 2013. (SCI)
73.
Y. C. Chang, C. L. Lin and T. Jennawasin, “Design of synthetic genetic oscillators based on RSGA,” Evolutionary Bioinformatics, no. 9, pp. 137-150, 01 2013.
74.
C. H. Chuang, C. L. Lin, Y. C. Chang, T. Jennawasin and P. K. Chen, “Design of synthetic biological logic circuits based on evolutionary algorithm,” IET Systems Biology, vol. 4, no. 7, 01 2013. (SCI)
75.
Y. K. Wu, C. C. Huang and C. L. Lin, “Resolution of the unit commitment problems by using the hybrid Taguchi-Ant colony system algorithm,” Electrical Power and Energy Systems, no. 49, pp. 188-198, 01 2013. (SCI)
76.
C. K. Chen, C. L. Lin, C. T. Chiang and S. L. Lin, “Information Encryption Using ECG Signals with Chaotic Functions and Transmissions via Synchronized Circuits,” IET Information Security, 01 2013.
77.
P. M. Hsu, C. L. Lin and M. Y. Yang, “On the complete coverage path planning for mobile robots,” Journal of Intelligent and Robotic Systems, 01 2013. (SCI)
78.
C. K. Chen, C. L. Lin, S. L. Lin, Y. M. Chiu and C. T. Chiang, “A chaotic Theoretical approach to ECG-based identity recognition,” IEEE Computational Intelligence Magazine, 01 2013.
79.
C. H. Juang and C. L. Lin, “Robust estimation of stochastic gene-network systems,” Journal of Biomedical Science and Engineering, no. 60, pp. 213-222, 01 2013.
80.
Y. P. Lin, C. L. Lin and Y. H. Li, “Development of 3-D modified proportional navigation guidance law against high-speed targets,” IEEE Transactions on Aerospace and Electronic Systems, vol. 1, no. 49, pp. 677-687, 01 2013. (SCI)
81.
B. R. Ke, C. L. Lin, C. P. Wang and F. Cao, “Optimization of fuel efficiency for freeway vehicles,” IET Intelligent Transport Systems, 01 2013. (SCI)
82.
P. M. Hsu and C. L. Lin, “Queue oscillation suppression in large-scale networks by extended network disturbance,” IET Control Theory and Applications, 01 2013.
83.
P. Suebsaiprom, C. L. Lin and S. Saimerk, “Fish robot modeling and simulation: Fish–tail and rigid-body motion,” International Journal of Advancements in Computing Technology, vol. 18, no. 4, pp. 105-114, 01 2012.
84.
C. C. Yang and C. L. Lin, “Robust adaptive sliding mode control for synchronization of space-clamped FitzHugh-Nagumo neurons,” Nonlinear Dynamics, no. 69, pp. 2089-2096, 01 2012.
85.
J. Y. Wu, S. P. Hsu, C. L. Lin and Y. J. Peng, “Balancing charge/discharge management for series/parallel battery packs,” Journal of Engineering, National Chung Hsing University, vol. 1, no. 23, pp. 13-26, 01 2012.
86.
V. T. Liu, C. L. Lin and H. Y. Wing, “New realization of Preisach model using adaptive polynomial approximation,” International Journal of Systems Science, vol. 9, no. 43, pp. 642-1649, 01 2012. (SCI)
87.
C. F. Hsu, C. L. Lin, W. C. Kao, Y. J. Tsai and H. M. Chen, “A biking route planning method for cyclists,” Journal of Technology, vol. 33, no. 27, pp. 153-160, 01 2012.
88.
C. K. Chen, C. L. Lin, C. T. Chiang and S. L. Lin, “Personalized information encryption using ECG signals with chaotic functions,” Information Sciences,, no. 193, pp. 125-140, 01 2012. (SCI)
89.
B. R. Ke, C. L. Lin and C. C. Yang, “Optimization of train energy-efficient operation for mass rapid transit systems,” IET Intelligent Transport Systems, vol. 1, no. 6, pp. 58-66, 01 2012. (SCI)
90.
C. L. Lin, T.C. Kao, C. S. Lee and C. H. Huang, “Evolutionary flight route planner for UAVs using potential field approach,” AIAA Journal of Aerospace Computing, Information, and Communication, vol. 3, no. 9, pp. 92-109, 01 2012. (SCI)
91.
林俊良、黃啟東, “電動機車電能回充控制器,” 中華民國發明專利 (專利號碼: I352671), 01 2011.
92.
C. H. Yu and C. L. Lin, “Power-RED: a novel algorithm to achieve bandwidth fairness,” IET Networks, 01 2011.
93.
C. S. Lee, C. L. Lin, V. T. Liu, C. C. Chen, W. S. Chen and H. J. Lin, “Implementation of multi-mini UAV navigation control system,” Journal of Aeronautics, Astronautics and Aviation, vol. 2, no. 43, pp. 129-136, 01 2011. (EI)
94.
C. H. Huang and C. L. Lin, “Evolutionary neural networks and DNA computing algorithms for dual-axis motion control,” Engineering Applications of Artificial Intelligence, no. 24, pp. 1263-1273, 01 2011. (SCI)
95.
C. L. Lin, C. H. Huang, C. S. Lee and M. J. Chao, “Identification of flight vehicle models using fuzzified eigensystem realization algorithm,” IEEE Transactions on Industrial Electronics, vol. 11, no. 58, pp. 5206-5219, 01 2011. (SCI)
96.
P. M. Hsu and C. L. Lin, “Congestion control mechanism concerning queue oscillation avoidance: a backstepping control approach,” Automatica,, 01 2011.
97.
C. H. Huang, C. L. Lin and M. J. Chao, “FERA in parameter identification with application in low speed wind tunnel test,” Aerospace Science and Technology, no. 15, pp. 495-509, 01 2011. (SCI)
98.
B. R. Ke, C. L. Lin and C. W. Lai, “Optimisation of train-speed trajectory and control for mass rapid transit systems,” Control Engineering Practice, vol. 7, no. 19, pp. 675-687, 01 2011. (SCI)
99.
C. L. Lin, “Congestion control for large-scale network with active queue management,” Engineering Science and Technology Bulletin, no. 114/115, pp. 41, 01 2011.
100.
C. W. Tsai, C. L. Lin and C. H. Huang, “Microbrushless DC motor control design based on real coded structural genetic algorithm,” IEEE/ASME Transactions on Mechatronics, vol. 1, no. 16, 01 2011. (SCI)
101.
P. M. Shiu, C. L. Lin and C. H. Yu, “Active queue management within large-scale wired networks,” International Journal of Communications, Network and System Sciences, no. 4, pp. 241-248, 01 2011. (EI)
102.
C. T. Huang, C. L. Lin and W. C. Lin, “Efficient energy managing control for electrical scooters,” IET Electrical Systems in Transportation, vol. 1, no. 2, pp. 9-17, 01 2010. (SCI)
103.
C. H. Chuang and C. L. Lin, “On robust state estimation of gene networks,” Biomedical Engineering and Computational Biology, no. 2, pp. 22-36, 01 2010.
104.
C. L. Lin, S. L. Hsiao and C. K. Chen, “Balance of emulated MDOF human postural systems,” International Journal of Engineering Science, no. 48, pp. 751-770, 01 2010. (SCI)
105.
C. L. Lin, “Analysis and design of advanced controllers for biological systems,” Engineering Science and Technology Bulletin, no. 107, 01 2010.
106.
C. L. Lin and C. H. Chuang, “Review of control theory and dynamics in systems biology,” International Journal of Systems and Synthetic Biology, vol. 1, no. 1, pp. 39-61, 01 2010.
107.
V. T. Liu, C. H. Liu, H. W. Li, C. L. Chen, C. L. Lin and Y. C. Lin, “Measurement and tracking control of the Z-tilt error compensating stage of the nano-measuring machine,” The International Journal of Systems & Cybernetics, vol. 6, no. 39, pp. 1029-1039, 01 2010. (SCI)
108.
Y. P. Lin, L. P. Tsao and C. L. Lin, “Development of three-dimensional aiming point guidance law,” International Journal of Systems Science, vol. 11, no. 41, pp. 1353-1362, 01 2010. (SCI)
109.
N. Aouf, M. Kharbat and C. L. Lin, “Video detection, tracking and path planning for ground autonomous systems,” International Journal of Computational Intelligence in Control, vol. 2, no. 1, pp. 85-94, 01 2009.
110.
P. A. Juang and C. L. Lin, “The electro-mechanical transfer function of an ultrasonic wheel system,” Measurement, no. 42, pp. 1417-1425, 01 2009. (SCI)
111.
C. W. Tsai, C. H. Huang and C. L. Lin, “Structure-specified IIR filter and control design using real structured genetic algorithm,” Applied Soft Computing, no. 9, pp. 1285-1295, 01 2009. (SCI)
112.
C. L. Lin, Y. W. Liu and C. H. Chuang, “Control design for signal transduction networks,” Bioinformatics and Biology Insights, no. 3, pp. 1-14, 01 2009.
113.
M. W. Hong, C. L. Lin, B. M. Shiu and N. Aouf, “Stabilizing networked pneumatic control systems with time-delays,,” International Journal of Computational Intelligence and Applications, vol. 2, no. 8, pp. 209-223, 01 2009. (EI)
114.
C. K. Lee, C. L. Lin and B. M. Chen, “Autonomous vehicle parking using hybrid artificial intelligent approach,” Journal of Intelligent and Robotic Systems, no. 56, pp. 319-343, 01 2009. (SCI)
115.
Y. C. Lin and C. L. Lin, “Optimal control approach for robust control design of neutral systems,” Optimal Control, Applications and Methods,, no. 30, pp. 319-343, 01 2009. (SCI)
116.
B. R. Ke, M. C. Chen and C. L. Lin, “Block-layout design using MAX-MIN ant system for saving energy on mass rapid transit systems,” IEEE Transactions on Intelligent Transportation Systems, vol. 2, no. 10, pp. 226-235, 01 2009. (SCI)
117.
M. W. Hong and C. L. Lin and B. M. Shiu, “Stabilizing network control for pneumatic systems with time-delays,” Mechatronics, no. 19, pp. 399-409, 01 2009.
118.
C. L. Lin, Y. P. Lin and K. M. Chen, “On the design of fuzzified trajectory shaping guidance law,” ISA Transactions, vol. 2, no. 48, 01 2009. (SCI)
119.
H. Y. Jan, C.L. Lin and T. S. Hwang, “Design of reduced-order controller by using DNA computing approach,” Applied Intelligence, 01 2009.
120.
C. H. Huang, H. Y. Jan, C. L. Lin and C. S. Lee, “System identification: DNA computing approach,” ISA Transactions, no. 48, pp. 254-263, 01 2009. (SCI)
121.
C. L. Lin, Y.P. Lin and T. L. Wang, “A fuzzy guidance law for vertical launch interceptors,” Control and Engineering Practice, no. 17, pp. 914-923, 01 2009. (SCI)
122.
C. L. Lin, Y. W. Liu and C. H. Chuang, “Analysis of signal transduction networks in Michaelis-Menten equations and S-systems,” International Journal of Biology and Biomedical Engineering, vol. 2, no. 2, 01 2008.
123.
C. H. Huang, C. L. Lin and H. Y. Jan, “Identification and control using DNA computing algorithms,” International Journal of Biology and Biomedical Engineering, vol. 3, no. 2, pp. 108-117, 01 2008.
124.
C. L. Li, C. L. Lin and C. K. Chen, “Stabilizing postural control for emulated human balancing systems,” International Journal of Engineering Science, vol. 11, no. 46, pp. 1120-1135, 01 2008.
125.
C. S. Chen, C. L. Lin and C. N. Chen, “Design of robust and economy speed controllers for electric scooters,” Journal of Vehicular Engineering, vol. 5, no. 5, pp. 143-164, 01 2008.
126.
H.Y. Jan, C. L. Lin, C. H. Huang and T. S. Hwang, “Robust motion control design for dual-axis motion platform using evolutionary algorithm,” Sadhana-Academy Proceedings in Engineering Sciences, vol. 6, no. 33, pp. 803-820, 01 2008. (SCI)
127.
C. L. Lin, C. H. Chen, and H. C. Huang, “Stabilizing control of networks with uncertain time-varying communication delays,” Control Engineering Practice, no. 16, pp. 56-66, 01 2008. (SCI)
128.
C. L. Lin, H. J. Jan, J. R. Lin and T. S. Hwang, “Singularity characterization and path planning of a new 3 links 6-DOFs parallel manipulator,” European Journal of Control, vol. 3, no. 14, 01 2008.
129.
C. L. Lin and C. T. Liu, “Failure detection and adaptive compensation for fault tolerable flight control systems,” IEEE Transactions on Industrial Informatics, vol. 4, no. 3, pp. 322-331, 01 2007. (SCI)
130.
H. C. Huang, C. L. Lin and M. W. Hong, “Design and realization of stabilizing network control systems with uncertain time-varying communication delays,” Journal of Engineering, National Chung Hsing University, vol. 3, no. 18, pp. 151-166, 01 2007.
131.
C. S. Chen and C.L. Lin, “An efficient energy managing controller for electric scooters,” International Journal of Electrical Engineering, 01 2007.
132.
C. L. Lin, J. R. Lin and H. Y. Jan, “Singularity analysis and path planning for a MDOF manipulator,” Journal of the Chinese Institute of Engineers, vol. 5, no. 30, pp. 917-922, 01 2007. (SCI)
133.
V. T. Liu, H. C. Huang, C. L. Lin and Z. J. Jian, “Neural net-based modeling and control of a micro-positioning platform using piezoelectric actuators,” Journal of Vibration and Control, vol. 3, no. 13, pp. 309-325, 01 2007. (SCI)
134.
Y. C. Lin, C. L. Lin, and C. C. Yang, “Robust active vibration control for rail vehicle pantograph,” IEEE Transactions on Vehicular Technology, vol. 4, no. 56, pp. 1994-2004, 01 2007. (SCI)
135.
C.L. Lin, W.C. Chang, and C.H. Chen, “A new dither-based friction compensation scheme,” Automatica, 01 2007.
136.
C.H. Chen, C.L. Lin and T. S. Hwang, “Stability of networked control systems with time-varying delays,” IEEE Communications Letters, vol. 3, no. 11, pp. 270-272, 01 2007. (SCI)
137.
C.L. Lin and T.L. Wang, “Fuzzy side force control for missile against hypersonic target,” IET Control Theory and Applications, vol. 1, no. 1, pp. 33-43, 01 2007. (SCI)
138.
C. L. Lin and C. T. Liu, “Failure detection and adaptive compensation for fault tolerable flight control systems,” IEEE Transactions on Industrial Informatics, vol. 4, no. 3, 01 2007.
139.
C.L. Lin and C. H. Chen, “Robust control of interconnected network schemes subject to random time-varying communication delays,” AEU International Journal of Electronics and Communications, no. 60, pp. 647-658, 01 2006. (SCI)
140.
Y.C. Lin, C.L. Lin and N.C. Shieh, “A hybrid evolutionary approach for robust active suspension design of light rail vehicles,” IEEE Transactions on Control Systems Technology, vol. 4, no. 14, 01 2006.
141.
Y. C. Lin, C. L. Lin and N. C. Shieh, “An evolutionary approach to active suspension design of rail vehicles,” Journal of the Chinese Institute of Engineers, vol. 5, no. 29, 01 2006. (SCI)
142.
C. L. Lin, K. M. Chen, M. T. Wu and S. W. Hwang, “Hybrid guidance law for interception of ballistic target,” Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering, no. 220, pp. 525-536, 01 2006. (SCI)
143.
H. Y. Jan, C. L. Lin and T. S. Hwang, “Self-organized PID control design using DNA computing approach,” Journal of the Chinese Institute of Engineers, vol. 2, no. 29, pp. 251-261, 01 2006. (SCI)
144.
C. L. Lin, H. Y. Jan, and T. S. Hwang, “Structure optimization of PID controllers based on DNA coding method,” Optimal Control, Applications and Methods, 01 2006.
145.
H.Y. Jan, C. L. Lin, C. H. Hwang, “Decoupling control design for dual axes platforms,” Journal of the Chinese Society of Mechanical Engineers, vol. 6, no. 26, pp. 741-745, 01 2005.
146.
C. L. Lin, H. Y. Jan, and T. S. Hwang, “Optimal path planning on 3D space using a DNA computing algorithm,” IEEE Transactions on Systems, Man, and Cybernetics, Pt. B, 01 2005.
147.
C.L. Lin and H. Y. Jan, “Mixed / multiobjective PID control for a linear brushless DC Motor: An evolutionary approach,” Control and Intelligent Systems, vol. 2, no. 33, 01 2005. (SCI)
148.
C.L. Lin and C.H. Chen, “A neural net-based time-delay compensation scheme and disturbance rejection for pneumatic systems,” IEEE Transactions on Neural Networks, 01 2004.
149.
V.T. Liu, C.L. Lin and G.P. Lee, “Neural net-based identification and control of a thin plate using piezoelectric actuators and sensors,” International Journal of Systems Science, vol. 15, no. 6, pp. 355-373, 01 2004. (SCI)
150.
C.L. Lin, H.Z. Hung, Y.Y. Chen and B.S. Chen, “Development of an integrated fuzzy-logic-based missile guidance law against high speed target,” IEEE Transactions on Fuzzy Systems, vol. 2, no. 12, pp. 157-169, 01 2004. (SCI)
151.
N.C. Hsieh, C.L. Lin and Y.C. Lin, “Optimal design for passive suspension of a light rail vehicle using constrained multiobjective evolutionary,” Journal of Sound and Vibration, accepted., 01 2004. (SCI)
152.
C.L. Lin, T.H. Hwang and R.C. Tsai, “Modeling and simulation of a linear motors-based platform manipulator,” International Journal of Modeling and Simulation, submitted, 01 2004.
153.
C. L. Lin, C. H. Chen and V. T. Liu, “A new time-delay compensating scheme for electro-hydraulic systems,” International Journal of Fluid Power, accepted, 01 2004.
154.
C. L. Lin, T. R. Lin and R. C. Tsai, “Singularity characterization and optimal path planning for a mixed linear and rotary motors-based dynamic platform,” JSME International Journal, Series C, submitted, 01 2004.
155.
C.L. Lin and C.L. Huang, “Design of a new fuzzy terminal guidance law,” International Journal of Systems Science, submitted, 01 2004.
156.
C. L. Lin, H. Y. Jan, and T. S. Hwang, “Novel self-organizing PID control design based on DNA coding method,” IEEE Trans. Evolutionary Computation, submitted, 01 2004.
157.
C. L. Lin, T. S. Hwang, and C. T. Liu, “Failure detection and adaptive compensation for fault tolerable flight control systems,” IEEE Trans. Industrial Applications, submitted, 01 2004.
158.
C. L. Lin, W. C. Shi, C. L. Hwang and H. C. Chang, “Design and analysis of a dithered radome error compensation scheme,” IEEE Trans. Control Systems Technology, submitted, 01 2004.
159.
C. L. Lin, H. Y. Jan, and T. S. Hwang, “Optimal path planning on 3D space using a DNA computing algorithm,” IEEE Trans. Systems, Man, and Cybernetics, Pt. B, submitted, 01 2004.
160.
C. L. Lin, H. Y. Jan and T. S. Hwang, “Self-Organized PID control design with application to linear transportation system,” EEE/ASME Trans. Mechatronics, submitted, 01 2004.
161.
C.L. Lin and K.M. Chen, “Hybrid guidance law for interception of ballistic target,” AIAA Journal of Guidance, Control, and Dynamics, submitted, 01 2004.
162.
C.L. Lin, H.Z. Hung and T.L. Wang, “Fuzzy side force control for missile against hypersonic target,” IEE Proceedings-Control Theory and Applications, submitted, 01 2004.
163.
C.L. Lin and H.Y. Jan, “New stability conditions for discrete singularly perturbed systems,” Transactions of the Chinese Institute of Electrical Engineering, vol. 3, no. 10, pp. 259-268, 01 2003. (EI)
164.
C.L. Lin and S.W. Huang, “Control for uncertain plants using confined adaptive fuzzy inference systems,” International Journal of Fuzzy Systems, vol. 4, no. 5, pp. 212-220, 01 2003. (SCI)
165.
T.H. Hwang, C.L. Lin and R.C. Tsai, “Analysis and design for a linear motors based parallel manipulator,” International Journal of Robotics and Automation, vol. 3, no. 18, pp. 97-110, 01 2003.
166.
C.L. Lin, V. T. Liu and G.P. Lee, “Identification and control of a benchmark flexible structure using piezoelectric actuators and sensors,” Journal of Vibration and Control, vol. 12, no. 9, pp. 1401-1420, 01 2003. (SCI)
167.
C.L. Lin, H. Y. Jan and N.C. Hsieh, “GA-based multiobjective PID control for a linear brushless DC motor,” IEEE/ASME Transactions on Mechatronics, vol. 1, no. 8, pp. 56-65, 01 2003. (SCI)
168.
C.L. Lin, “On the design of a 6DOF mixed linear and rotatory motor-based dynamic platform,” Engineering Science and Technology Bulletin, no. 68, pp. 97-100, 01 2003.
169.
C.L. Lin and C.L Huang, “A dynamically fuzzy gain-scheduled design for missile autopilot,” The Aeronautical Journal, vol. 1076, no. 107, pp. 599-606, 01 2003. (SCI)
170.
C.L. Lin, T.H. Hwang and R.C. Tsai, “Adaptive control for a mixed linear and rotary motors-based dynamic platform,” IEEE Transactions on Control Systems Technology, 01 2003. (SCI)
171.
B.S. Chen, Y.Y. Chen and C.L. Lin, “Nonlinear fuzzy H guidance law with saturation of actuators against maneuvering targets,” IEEE Transactions on Control Systems Technology, vol. 6, no. 10, pp. 769-779, 01 2002. (SCI)
172.
C.L. Lin, N.C. Shieh and P.C. Tung, “position control of linear brushless DC motor using wavelet controller,” IEEE Transactions on Aerospace and Electronic Systems, vol. 3, no. 38, pp. 918-932, 01 2002. (SCI)
173.
C.L. Lin and H.T. Huang, “Linear servo motor control using adaptive neural networks,” IME Journal of Systems and Control Engineering, no. 216, pp. 407-427, 01 2002. (SCI)
174.
C.L. Lin, “Precision servo control for a linear brushless motor,” Engineering Science and Technology Bulletin, no. 60, pp. 23-27, 01 2002.
175.
C.L. Lin and T.Y. Lin, “Neural net-based control for a class of nonlinear systems,” Neural Processing Letters, vol. 2, no. 15, pp. 157-177, 01 2002. (SCI)
176.
C.L. Lin and R.M. Lai, “A novel approach to guidance and control system design using genetic-based fuzzy logic model,” IEEE Transactions on Control Systems Technology, vol. 4, no. 10, pp. 600-610, 01 2002. (SCI)
177.
N.C. Shieh, P.C. Tung and C.L. Lin, “Robust output tracking control of a linear brushless DC motor with time-varying disturbances,” IEE Proceedings-Electric Power Applications, vol. 1, no. 149, pp. 39-45, 01 2002. (SCI)
178.
C.L. Lin and T.Y. Lin, “Approach to adaptive neural net-based control design,” IEE Proceedings-Control Theory and Applications, vol. 4, no. 149, pp. 331-342, 01 2002. (SCI)
179.
M.T. Wu, F.L. Hu and C.L. Lin, “Anti-lock braking system for unmanned aerial vehicle,” Transactions of the Aeronautical and Astronautical Society of the Republic of China, vol. 2, no. 34, pp. 167-177, 01 2002. (EI)
180.
C.L. Lin and H.Z. Haung, “An novel anti-lock brake system using fuzzy inference system: analysis and design,” Journal of Technology, vol. 1, no. 17, pp. 21-30, 01 2002.
181.
N.C. Hsieh, C.T. Chang, C.L. Lin and H.Y. Jan, “Robust position control of a transportation carriage directly driven by linear motor using wavelet neural network,” Engineering Applications of Artificial Intelligence, no. 15, pp. 479-489, 01 2002. (SCI)
182.
C.L. Lin and H.Y. Jan, “Multiobjective PID control for a linear brushless DC motor: an evolutionary approach,” IEE Proceedings-Electric Power Applications, vol. 6, no. 149, pp. 397-406, 01 2002. (SCI)
183.
C.L. Lin, “Stability analysis of radome error and calibration using neural networks,” IEEE Transactions on Aerospace and Electronic Systems, vol. 4, no. 37, pp. 1442-1450, 01 2001. (SCI)
184.
C.L. Lin and H.W. Su, “Adaptive fuzzy gain scheduling in guidance system design,” AIAA Journal of Guidance, Control, and Dynamics, vol. 4, no. 24, pp. 683-692, 01 2001. (SCI)
185.
C.L. Lin and Y.H. Hsiao, “Adaptive feedforward control for disturbance torque rejection in seeker stabilizing loop,” IEEE Transactions on Control Systems Technology, vol. 1, no. 9, pp. 108-121, 01 2001. (SCI)
186.
C.L. Lin, “Neural networks for matrix scaling problem solving,” Asian Journal of Control, vol. 4, no. 3, pp. 289-299, 01 2001. (EI)
187.
C.L. Lin and R.M. Lai, “Parameter design for guidance and control system using genetic approach,” Aerospace Science and Technology, vol. 6, no. 5, pp. 425-434, 01 2001. (SCI)
188.
C.L. Lin and C.L. Chen, “Realisation of a Riccati equation-based controller using gradient-type neural networks,” Control Engineering Practice, no. 6, pp. 329-341, 01 2001. (SCI)
189.
C.L. Lin and T.Y. Lin, “An design approach for neural net-based control schemes,” IEEE Transactions on Automatic Control, vol. 10, no. 46, pp. 1599-1605, 01 2001. (SCI)
190.
C.L. Lin and P.S. Hao, “Robust fuzzy control of a vibrating thin plate,” JSME International Journal, Series C, vol. 2, no. 44, pp. 315-326, 01 2001. (SCI)
191.
B.S. Chen, Y.Y. Chen and C.L. Lin, “Nonlinear robust guidance law against maneuvering targets: fuzzy observer-based feedback approach,” IEEE Transactions on Aerospace and Electronic Systems, 01 2001.
192.
V.T. Liu, C.L. Lin, L.C. Shiue and H.W. Su, “Design of fuzzy-PD based guidance law,” Journal of Technology, vol. 1, no. 15, pp. 113-121, 01 2000.
193.
C.L. Lin, “Neural net-based adaptive LQ control,” Optimal Control and Applications, 01 2000.
194.
C.L. Lin and H.W. Su, “control theory in guidance and control system design: an overview,” Proceedings of the National Science Council, R.O.C., Part A, vol. 1, no. 24, pp. 15-30, 01 2000. (EI)
195.
C.L. Lin and Y.Y. Chen, “Design of fuzzy logic guidance law against high-speed target,” AIAA Journal of Guidance, Control, and Dynamics, vol. 1, no. 23, pp. 17-25, 01 2000. (SCI)
196.
C.L. Lin, C. C. Lai and T.H. Huang, “A neural network for linear matrix inequality problems,” IEEE Transactions on Neural Networks, vol. 5, no. 11, pp. 1078-1092, 01 2000. (SCI)
197.
C.L. Lin and T.H. Huang, “ novel approach solving for linear matrix inequalities using neural networks,” Neural Processing Letters, vol. 2, no. 11, pp. 153-169, 01 2000. (SCI)
198.
C.L. Lin, V.T. Liu and P.S. Hao, “Robust neuro control for rotating disk vibrations,” IME Journal of Mechanical Science Engineering, no. 214, pp. 1529-1544, 01 2000. (SCI)
199.
C.L. Lin, “On stability of linear uncertain descriptor systems,” Journal of The Franklin Institute, no. 336, pp. 549-564, 01 1999. (SCI)
200.
C.L. Lin and C.Y. Chung, “Stability of linear constrained dynamical systems with modeling uncertainty,” Journal of the Chinese Society of Mechanical Engineers, vol. 1, no. 20, pp. 87-95, 01 1999. (EI)
201.
C.L. Lin and Y.Y. Chen, “of an advanced guidance law against high speed attacking targe,” Proceedings of the National Science Council, R.O.C., Part A, vol. 1, no. 23, pp. 60-74, 01 1999. (EI)
202.
C.Y. Chung and C.L. Lin, “A transformed Lur’e problem for sliding mode control and chattering reduction,” IEEE Transactions on Automatic Control, vol. 3, no. 44, pp. 563-568, 01 1999. (SCI)
203.
C.L. Lin, V.T. Liu and H.W. Su, “A novel design approach for fuzzy guidance law,” Transactions of the Aeronautical and Astronautical Society of the Republic of China, vol. 2, no. 31, pp. 107-115, 01 1999. (EI)
204.
C.L. Lin and T.H. Huang, “Realization of electronic neural network for solving Lyapunov matrix equation,” Transactions of the Chinese Institute of Electrical Engineering, vol. 4, no. 6, pp. 331-338, 01 1999. (EI)
205.
C.L. Lin and W.R. Hsiao, “net-based compensator design for radome refraction slope error,” Journal of Feng Chia University, no. 35, pp. 93-112, 01 1999.
206.
C.L. Lin, “On the study of optimal guidance design against high speed attacking target,” Engineering Science and Technology Bulletin, no. 35, pp. 15-18, 01 1999.
207.
C.L. Lin, “Control of perturbed systems using neural networks,” Transactions on Neural Networks, vol. 5, no. 9, pp. 1046-1050, 01 1998. (SCI)
208.
C.L. Lin, “Synthesis of real-time robust flexible structure controllers,” AIAA Journal of Guidance, Control, and Dynamics, vol. 6, no. 21, pp. 1001-1004, 01 1998. (SCI)
209.
C.L. Lin, V.T. Liu and H.W. Su, “Design of fuzzy logic-based guidance and control systems,” Journal of the Chinese Fuzzy Systems Association, vol. 2, no. 4, pp. 1-14, 01 1998.
210.
C.L. Lin and T.J. Chen, “Recurrent neural networks for stability verification of uncertain singular systems,” Journal of Control Systems and Technology, vol. 2, no. 6, pp. 25-35, 01 1998. (EI)
211.
C.L. Lin and V.T. Liu, “tability and performance analyses of radome refraction slope errors and time-to-go on aerodynamically controlled missiles,” Transactions of the Aeronautical and Astronautical Society of the Republic of China, vol. 1, no. 28, pp. 71-80, 01 1996.
212.
C.L. Lin, “On the study of nonlinear behavior for tactical missile systems using statistical linearization technique,” Journal of Feng Chia University, vol. 1, no. 29, pp. 265-283, 01 1996.
213.
C.L. Lin, “Stabilizing control of discrete-time singularly perturbed systems,” International Journal of Systems Science, vol. 12, no. 27, pp. 1473-1482, 01 1996. (SCI)
214.
C.L. Lin, “Perturbation analysis for flexible system control,” Journal of Guidance, Control, and Dynamics, vol. 3, no. 18, pp. 633-635, 01 1995. (SCI)
215.
C.Y. Chung and C. L. Lin, “A general class of sliding surface for sliding mode control,” IEEE Transactions on Automatic Control, vol. 1, no. 43, pp. 115-119, 01 1995. (SCI)
216.
C.L. Lin, “Robust design criteria for active control of flexible systems,” International Journal of Systems Science, vol. 3, no. 25, pp. 483-501, 01 1994. (SCI)
217.
V.T. Liu and C.L. Lin, “Robust stabilization for composite observer-based control of discrete systems,” Automatica, vol. 5, no. 30, pp. 877-881, 01 1994. (SCI)
218.
C.L. Lin and B.S. Chen, “Robust observer-based control of large flexible structures,” ASME Journal of Dynamic Systems, Measurement, no. 116, pp. 713-722, 01 1994. (SCI)
219.
C.L. Lin, “Stabilization of singularly perturbed large-scale interconnected discrete-time systems,” Journal of The Franklin Institute, vol. 4, no. 331B, pp. 329-344, 01 1994. (SCI)
220.
C.L. Lin, “Design of flexible structure control system using constrained controls,” Transactions of the Aeronautical and Astronautical Society of the Republic of China, vol. 4, no. 26, pp. 319-327, 01 1994.
221.
V.T. Liu and C.L. Lin, “Application of generalized model matching control for missile autopilot design,” Journal of Technology, vol. 2, no. 8, pp. 237-246, 01 1993.
222.
C.L. Lin, F.B. Hsiao, L. R. Tsuei, and B. S. Chen, “controller design of a single-link robot arm,” Journal of the Chinese Institute of Engineers, vol. 2, no. 16, pp. 171-193, 01 1993. (SCI)
223.
C.L. Lin and V.T. Liu, “Robustness of feedback control for discrete two-time-scale systems,” Journal of the Chinese Institute of Engineers, vol. 5, no. 16, pp. 709-719, 01 1993. (SCI)
224.
C.L. Lin, “Robust control of flexible structures using residual mode filters,” Journal of Guidance, Control, and Dynamics, vol. 5, no. 16, pp. 973-977, 01 1993. (SCI)
225.
C.L. Lin and V.T. Liu, “Stabilization of flexible systems under a certain class of nonlinear feedback controls,” Transactions of Nanging University of Aeronautics and Astronautics, vol. 1, no. 10, pp. 25-29, 01 1993.
226.
C.L. Lin and V.T. Liu, “Synthesis of generalized model matching controller and its application to autopilot design,” Transactions of the Aeronautical and Astronautical Society of the Republic of China, vol. 2, no. 25, pp. 129-142, 01 1993.
227.
C.L. Lin and B.S. Chen, “On the design of stabilizing controllers for singularly perturbed systems,” IEEE Transactions on Automatic Control, vol. 11, no. AC-37, pp. 1828-1834, 01 1992. (SCI)
228.
F.B. Hsiao and C.L. Lin, “Model matching systems: necessary and sufficient conditions for stability under plant perturbations,” International Journal of Systems Science, vol. 5, no. 22, pp. 1991, 01 1991. (SCI)
229.
C.L. Lin, B.S. Chen, and F.B. Hsiao, “On stability and stabilization of mechanical structures under nonlinear time-varying perturbations,” Journal of Applied Mechanics, vol. 2, no. 58, pp. 527-535, 01 1991. (SCI)
230.
B.S. Chen, C.L. Lin, and F.B. Hsiao, “Robust observer-based control of a vibrating beam,” IME Journal of Mechanical Science Engineering, vol. C2, no. 205, pp. 77-89, 01 1991. (SCI)
231.
C.L. Lin, F.B. Hsiao, and B.S. Chen, “condition for flexible structure control with mode residualization,” AIAA Journal of Guidance, Control, and Dynamics, vol. 6, no. 13, pp. 1160-1163, 01 1990. (SCI)
232.
C.L. Lin, F.B. Hsiao, and B.S. Chen, “Stabilization of large structural systems under mode truncation, parameter perturbations, and actuator saturations,” International Journal of Systems Science, vol. 8, no. 20, pp. 1423-1440, 01 1990. (SCI)
233.
B.S. Chen and C.L. Lin, “On the stability bounds of singularly perturbed systems,” IEEE Transactions on Automatic Control, vol. 11, no. AC-35, pp. 1265-1270, 01 1990. (SCI)
234.
B.S. Chen and C.L. Lin, “Robust controllers for multivariable model matching systems,” International Journal of Control, vol. 5, no. 50, pp. 1717-1730, 01 1989. (SCI)
235.
J. J. Kao, C. L. Lin, C. C. Huang and Y. T. Kuo , “Bidirectional wireless power/data transfer via magnetic field ,” IET Journal of Engineering ,
236.
C. C. Yang and C. L. Lin, “Adaptive sliding mode control for chaotic synchronization of oscillator with input nonlinearity,” International Journal of Vibration and Control,
237.
Y. C. Liu, C. L. Lin and C. H. Chuang, “An Approach for model reduction of biochemical networks,” Computational Biology Journal,
238.
C. L. Lin, Y. H. Li and N. Aouf, “Potential-field-based evolutionary route planner for the control of multiple UAVs,” Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering, no. 224, pp. 1229-1242. (SCI)
239.
Y. C. Lin, C. L. Lin, W. C. Shi and S. W. Huang, “Dither-based compensating strategy for radome boresight error and gimbal friction,” Aeronautical Journal,, vol. 1138, no. 112.
"""

# 正則表達式匹配模式
pattern = re.compile(
    r'(.*?),\s*“(.*?)\s*,”\s*(.*?),\s*(?:vol\.\s*(\d+),\s*no\.\s*(\d+),)?(?:\s*pp\.\s*[\d\-]+,)?\s*(\d{2})\s*(\d{4})'
)

# 匹配數據
matches = pattern.findall(input_text)

# 準備 CSV 文件
output_csv = "publications.csv"

# 將匹配結果寫入 CSV
with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    # 寫入標題
    csvwriter.writerow(["authors", "title", "venue", "volume", "issue", "date"])
    for match in matches:
        authors, title, venue, volume, issue, month, year = match
        date = f"{year}-{month.zfill(2)}"
        venue_detail = f"{venue.strip()}"
        if volume and issue:
            venue_detail += f", vol. {volume}, no. {issue}"
        csvwriter.writerow([authors.strip(), title.strip(), venue_detail, volume, issue, date])

print(f"CSV file '{output_csv}' generated successfully!")
