# IEEE-CAA-paper-2025-Multi-interval-aggregation-failure-point-approximation-for-RUL-prediction

Remaining useful life prediction in CALCE battery and milling cutter dataset.

Paper: Multi-interval aggregation failure point approximation for RUL prediction

The website of the paper：https://ieeexplore.ieee.org/abstract/document/10664192


<img width="2110" height="964" alt="image" src="https://github.com/user-attachments/assets/b6f50dd2-722a-4557-a61e-c1e1ec1f57ad" />
<img width="704" height="702" alt="image" src="https://github.com/user-attachments/assets/5c1f827d-4570-4b76-b302-959b4cd2759c" />




# Easy to reproduce all details of our paper successfully
The downloaded compressed package can reproduce our method.To make code easy to run successfully, we debug the files carefully. Generally speaking, if environments are satisfied, you can directly run all the xxx.py files inside after decompressing the compressed package without changing any code.

(1) Download and rename xxx.zip to MFA.zip (Rename to avoid errors caused by long directories)

(2) Unzip MFA.zip

(3) Run any xxx.py directly


# Paper of Code and Citation
(1) To better understand our code, please read our paper.

Paper: IEEE-CAA-paper-2025-Multi-interval-aggregation-failure-point-approximation-for-RUL-prediction

The website of the paper：https://ieeexplore.ieee.org/abstract/document/10664192

(2) Please cite this paper and the original source of the dataset when using the code for academic purposes.

GB/T 7714: 
Fan L, Chen X, Li S, et al. Multi-interval-aggregation failure point approximation for remaining useful life prediction[J]. IEEE/CAA Journal of Automatica Sinica, 2025, 12(3): 639 - 641.


BibTex:

@ARTICLE{fan2025Multi,
  author={Fan, Linchuan and Chen, Xiaolong and Li, Shuo and Chai, Yi},
  journal={IEEE/CAA Journal of Automatica Sinica}, 
  title={Multi-Interval-Aggregation Failure Point Approximation for Remaining Useful Life Prediction}, 
  year={2025},
  volume={12},
  number={3},
  pages={639-641},
  publisher={IEEE},
  keywords={Degradation;Predictive models;Batteries;Accuracy;Milling;Market research;Logic gates},
  doi={10.1109/JAS.2024.124593}}



# Relationship between Code and Paper

 (1) TABLE 1 MFA-BiLSTM(Calce battery)
 
 :code\comparison experiments\cacle\MFA2025\BiLSTM_MF_grid.py  

 (2) TABLE 1 MFA-BiLSTM(Milling cutter)
 
 :code\comparison experiments\xiandao\MFA2025\BiLSTM_MF_grid.py  

 (3) Equation 7
 
 :code\comparison experiments\cacle\MFA2025\min_interation_times.py

......

# Environment and Acknowledgement:

(1) Environment:

tensorflow-gpu            1.15.0
    
keras                     2.2.4
    
scipy                     1.5.2
    
pandas                    1.0.5
    
numpy                     1.19.1


(2) Acknowledgement: 
Thanks for the following references sincerely.
   
M. Pecht, “Calce battery group,” 2017. [Online]. Available: http://www.calce.umd.edu/batteries/data.htm.
   
Prognostics and H. M. Society, “PHM data challenge 2010,” 2010. [Online]. Available: https://phmsociety.org/conference/.
   
