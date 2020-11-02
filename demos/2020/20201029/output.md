== Executing Script ==
# Introduction
CDF files were downloaded from https://cdaweb.gsfc.nasa.gov/pub/software/cdf/cdf_test_files 
and inspected to see if all the different features of CDF files are found.
# Files Used
a1_k0_mpa_20050804_v02.cdf<br>
ac_h2_sis_20101105_v06.cdf<br>
ac_or_ssc_20031101_v01.cdf<br>
ac_or_ssc_20040809_v01.cdf<br>
bigcdf_compressed.cdf<br>
c1_waveform_wbd_200202080940_v01.cdf<br>
c1_waveform_wbd_200202080940_v01_subset.cdf<br>
cl_jp_pgp_20031001_v52.cdf<br>
cl_sp_edi_00000000_v01.cdf<br>
cluster-2_cp3drl_2002052000000_v1.cdf<br>
de_uv_sai_19910218_v01.cdf<br>
ge_k0_cpi_19921231_v02.cdf<br>
i1_av_ott_1983351130734_v01.cdf<br>
im_k0_euv_20011231_v01.cdf<br>
im_k0_rpi_20051218_v01.cdf<br>
im_k1_rpi_20051217_v01.cdf<br>
mms1_fpi_fast_sitl_20150801132440_v0.0.0.cdf<br>
po_h4_pwi_19970901_v01.cdf<br>
po_h9_pwi_1997010103_v01.cdf<br>
po_k0_uvi_20051230_v02.cdf<br>
tha_l2_fgm_20070729_v01.cdf<br>
tha_l2_fgm_20101202_v01.cdf<br>
tha_l2_scm_20160831_v01.cdf<br>
timed_L1Cdisk_guvi_20060601005849_v01.cdf<br>
twins1_l1_imager_2010102701_v01.cdf<br>
ulysses.cdf<br>
# a1_k0_mpa_20050804_v02.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[2, 3]|0|CDF_EPOCH|16|
|Time_PB5|[2, 3]|0|CDF_INT4|24|
|dens_lop|[2, 3]|0|CDF_REAL4|8|
|vel_lop|[2, 3]|0|CDF_REAL4|24|
|temp_lop|[2, 3]|0|CDF_REAL4|16|
|tratio_lop|[2, 3]|0|CDF_REAL4|8|
|dens_hip|[2, 3]|0|CDF_REAL4|8|
|vel_hip|[2, 3]|0|CDF_REAL4|24|
|temp_hip|[2, 3]|0|CDF_REAL4|16|
|theta_phi_hip|[2, 3]|0|CDF_REAL4|16|
|tratio_hip|[2, 3]|0|CDF_REAL4|8|
|dens_e|[2, 3]|0|CDF_REAL4|8|
|temp_e|[2, 3]|0|CDF_REAL4|16|
|theta_phi_e|[2, 3]|0|CDF_REAL4|16|
|tratio_e|[2, 3]|0|CDF_REAL4|8|
|sc_pot|[2, 3]|0|CDF_REAL4|8|
|bkgd|[2, 3]|0|CDF_REAL4|8|
|sc_pos_geo|[2, 3]|0|CDF_REAL4|24|
no locator!
|sc_pos_mag|[2, 3]|0|CDF_REAL4|24|
|qual_flag|[2, 3]|0|CDF_INT4|8|
|gap_flag|[2, 3]|0|CDF_INT4|8|
|label_time|[2, 3]|0|CDF_CHAR|1|
|unit_time|[2, 3]|0|CDF_CHAR|1|
|format_time|[2, 3]|0|CDF_CHAR|1|
|offset_time|[2, 3]|0|CDF_REAL8|1|
|label_pos_l|[2, 3]|0|CDF_CHAR|1|
|unit_pos_l|[2, 3]|0|CDF_CHAR|1|
|angle_pos_l|[2, 3]|0|CDF_CHAR|1|
|label_possyn_l|[2, 3]|0|CDF_CHAR|1|
|unit_possyn_l|[2, 3]|0|CDF_CHAR|1|
|angle_possyn_l|[2, 3]|0|CDF_CHAR|1|
|label_pos_m|[2, 3]|0|CDF_CHAR|1|
|unit_pos_m|[2, 3]|0|CDF_CHAR|1|
|angle_pos_m|[2, 3]|0|CDF_CHAR|1|
|label_theta_phi|[2, 3]|0|CDF_CHAR|1|
|label_vel|[2, 3]|0|CDF_CHAR|1|
|Cartesian|[2, 3]|0|CDF_CHAR|1|
|label_temp|[2, 3]|0|CDF_CHAR|1|
# ac_h2_sis_20101105_v06.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|1|
|Time_PB5|[3]|0|CDF_INT4|1|
|unit_time|[3]|0|CDF_CHAR|1|
|label_time|[3]|0|CDF_CHAR|1|
|format_time|[3]|0|CDF_CHAR|1|
|flux_He|[8]|0|CDF_REAL4|2|
|label_ebands_flux_He|[8]|0|CDF_CHAR|1|
|flux_C|[8]|0|CDF_REAL4|2|
|label_ebands_flux_C|[8]|0|CDF_CHAR|1|
|flux_N|[8]|0|CDF_REAL4|2|
|label_ebands_flux_N|[8]|0|CDF_CHAR|1|
|flux_O|[8]|0|CDF_REAL4|2|
|label_ebands_flux_O|[8]|0|CDF_CHAR|1|
|flux_Ne|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ne|[8]|0|CDF_CHAR|1|
|flux_Na|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Na|[8]|0|CDF_CHAR|1|
|flux_Mg|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Mg|[8]|0|CDF_CHAR|1|
|flux_Al|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Al|[8]|0|CDF_CHAR|1|
|flux_Si|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Si|[8]|0|CDF_CHAR|1|
|flux_S|[8]|0|CDF_REAL4|2|
|label_ebands_flux_S|[8]|0|CDF_CHAR|1|
|flux_Ar|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ar|[8]|0|CDF_CHAR|1|
|flux_Ca|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ca|[8]|0|CDF_CHAR|1|
|flux_Fe|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Fe|[8]|0|CDF_CHAR|1|
|flux_Ni|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ni|[8]|0|CDF_CHAR|1|
|cnt_He|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_He|[8]|0|CDF_CHAR|1|
|cnt_C|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_C|[8]|0|CDF_CHAR|1|
|cnt_N|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_N|[8]|0|CDF_CHAR|1|
|cnt_O|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_O|[8]|0|CDF_CHAR|1|
|cnt_Ne|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ne|[8]|0|CDF_CHAR|1|
|cnt_Na|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Na|[8]|0|CDF_CHAR|1|
|cnt_Mg|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Mg|[8]|0|CDF_CHAR|1|
no locator!
|label_ebands_cnt_Al|[8]|0|CDF_CHAR|1|
|cnt_Si|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Si|[8]|0|CDF_CHAR|1|
|cnt_S|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_S|[8]|0|CDF_CHAR|1|
|cnt_Ar|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ar|[8]|0|CDF_CHAR|1|
|cnt_Ca|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ca|[8]|0|CDF_CHAR|1|
|cnt_Fe|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Fe|[8]|0|CDF_CHAR|1|
|cnt_Ni|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ni|[8]|0|CDF_CHAR|1|
# ac_or_ssc_20031101_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|XYZ_GSE|[3]|0|CDF_DOUBLE|198|
|cartesian|[3]|0|CDF_CHAR|1|
|xyz_lbl|[3]|0|CDF_CHAR|1|
|Epoch|[]|0|CDF_EPOCH|173|
|GSE_LAT|[]|0|CDF_FLOAT|87|
|GSE_LON|[]|0|CDF_FLOAT|87|
|RADIUS|[]|0|CDF_DOUBLE|173|
# ac_or_ssc_20040809_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|1|
|Time_PB5|[3]|0|CDF_INT4|1|
|unit_time|[3]|0|CDF_CHAR|1|
|label_time|[3]|0|CDF_CHAR|1|
|format_time|[3]|0|CDF_CHAR|1|
|flux_He|[8]|0|CDF_REAL4|2|
|label_ebands_flux_He|[8]|0|CDF_CHAR|1|
|flux_C|[8]|0|CDF_REAL4|2|
|label_ebands_flux_C|[8]|0|CDF_CHAR|1|
|flux_N|[8]|0|CDF_REAL4|2|
|label_ebands_flux_N|[8]|0|CDF_CHAR|1|
|flux_O|[8]|0|CDF_REAL4|2|
|label_ebands_flux_O|[8]|0|CDF_CHAR|1|
|flux_Ne|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ne|[8]|0|CDF_CHAR|1|
|flux_Na|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Na|[8]|0|CDF_CHAR|1|
|flux_Mg|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Mg|[8]|0|CDF_CHAR|1|
|flux_Al|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Al|[8]|0|CDF_CHAR|1|
|flux_Si|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Si|[8]|0|CDF_CHAR|1|
|flux_S|[8]|0|CDF_REAL4|2|
|label_ebands_flux_S|[8]|0|CDF_CHAR|1|
|flux_Ar|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ar|[8]|0|CDF_CHAR|1|
|flux_Ca|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ca|[8]|0|CDF_CHAR|1|
|flux_Fe|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Fe|[8]|0|CDF_CHAR|1|
|flux_Ni|[8]|0|CDF_REAL4|2|
|label_ebands_flux_Ni|[8]|0|CDF_CHAR|1|
|cnt_He|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_He|[8]|0|CDF_CHAR|1|
|cnt_C|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_C|[8]|0|CDF_CHAR|1|
|cnt_N|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_N|[8]|0|CDF_CHAR|1|
|cnt_O|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_O|[8]|0|CDF_CHAR|1|
|cnt_Ne|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ne|[8]|0|CDF_CHAR|1|
|cnt_Na|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Na|[8]|0|CDF_CHAR|1|
|cnt_Mg|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Mg|[8]|0|CDF_CHAR|1|
no locator!
|label_ebands_cnt_Al|[8]|0|CDF_CHAR|1|
|cnt_Si|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Si|[8]|0|CDF_CHAR|1|
|cnt_S|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_S|[8]|0|CDF_CHAR|1|
|cnt_Ar|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ar|[8]|0|CDF_CHAR|1|
|cnt_Ca|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ca|[8]|0|CDF_CHAR|1|
|cnt_Fe|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Fe|[8]|0|CDF_CHAR|1|
|cnt_Ni|[8]|0|CDF_REAL4|2|
|label_ebands_cnt_Ni|[8]|0|CDF_CHAR|1|
# bigcdf_compressed.cdf
Byte Order: LITTLE_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|temp|[1024, 768]|1|CDF_DOUBLE|400|
# c1_waveform_wbd_200202080940_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[2]|512000|CDF_EPOCH16|33|
|Bandwidth|[]|512000|CDF_REAL4|33|
|Translation|[]|512000|CDF_REAL4|33|
|Resolution|[]|512000|CDF_BYTE|33|
|ANTENNA|[]|512000|CDF_BYTE|33|
|Gain|[]|512000|CDF_BYTE|33|
|Ant_B_Field_Angle|[]|512000|CDF_REAL4|33|
|Ant_Xgse_Angle|[]|512000|CDF_REAL4|33|
|Ant_YZgse_Plane_Angle|[]|512000|CDF_REAL4|33|
|DC_Offset|[]|512000|CDF_REAL4|33|
|WBD_Elec|[]|512000|CDF_REAL4|33|
|WBD_Mag|[]|512000|CDF_REAL4|33|
|DATA_QUALITY|[]|512000|CDF_BYTE|33|
# c1_waveform_wbd_200202080940_v01_subset.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[2]|512000|CDF_EPOCH16|1|
|Bandwidth|[]|512000|CDF_REAL4|1|
|Translation|[]|512000|CDF_REAL4|1|
|Resolution|[]|512000|CDF_BYTE|1|
|ANTENNA|[]|512000|CDF_BYTE|1|
|Gain|[]|512000|CDF_BYTE|1|
|Ant_B_Field_Angle|[]|512000|CDF_REAL4|1|
|Ant_Xgse_Angle|[]|512000|CDF_REAL4|1|
|Ant_YZgse_Plane_Angle|[]|512000|CDF_REAL4|1|
|DC_Offset|[]|512000|CDF_REAL4|1|
|WBD_Elec|[]|512000|CDF_REAL4|1|
|WBD_Mag|[]|512000|CDF_REAL4|1|
|DATA_QUALITY|[]|512000|CDF_BYTE|1|
# cl_jp_pgp_20031001_v52.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|L_gse_xyz|[3]|0|CDF_CHAR|1|
|Half_interval__CL_JP_PGP|[]|0|CDF_REAL8|1|
|Epoch__CL_JP_PGP|[]|0|CDF_EPOCH|1|
|sc_orbit_num__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_r_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|L_sc_r_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|sc_v_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|L_sc_v_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|sc_dr1_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|sc_dr2_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|sc_dr3_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|sc_dr4_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|L_sc1_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|L_sc2_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|L_sc3_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|L_sc4_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|sc_at1_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at1_long__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at2_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at2_long__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at3_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at3_long__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at4_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_at4_long__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_config_QG__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_config_QR__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_dr_min__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_dr_max__CL_JP_PGP|[]|0|CDF_REAL4|1|
|gse_gsm__CL_JP_PGP|[]|0|CDF_REAL4|1|
|dipole_tilt__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_geom_size__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_geom_elong__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_geom_planarity__CL_JP_PGP|[]|0|CDF_REAL4|1|
|sc_geom_E_dir_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|L_geom_E_dir_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
|sc_geom_P_nor_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|
|L_geom_P_nor_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|
# cl_sp_edi_00000000_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|L_gse_xyz|[3]|0|CDF_CHAR|1|
|Half_interval__CL_SP_EDI|[]|0|CDF_REAL8|1|
no locator!
|Status__CL_SP_EDI|[7]|0|CDF_UINT1|1|
|L_Status_EDI_SP|[7]|0|CDF_CHAR|1|
no locator!
|L_V_ed_xyz_gse__CL_SP_EDI|[3]|0|CDF_CHAR|1|
# cluster-2_cp3drl_2002052000000_v1.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|226|
|Epoch_Start|[]|0|CDF_REAL8|1|
|Epoch_End|[]|0|CDF_REAL8|226|
|Mode_Epoch|[]|0|CDF_EPOCH|226|
|Mode_Epoch_Start|[]|0|CDF_REAL8|1|
|Mode_Epoch_End|[]|0|CDF_REAL8|226|
|Center_Scan|[93]|0|CDF_FLOAT|1|
|Band_Low_Scan|[93]|0|CDF_FLOAT|1|
|Band_High_Scan|[93]|0|CDF_FLOAT|1|
|1_C2 LEEA Zones 0-1|[93]|0|CDF_FLOAT|7206|
|1_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL1|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL1|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE1|[93]|0|CDF_FLOAT|7206|
|2_C2 LEEA Zones 2-3|[93]|0|CDF_FLOAT|7206|
|2_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL2|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL2|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE2|[93]|0|CDF_FLOAT|7206|
|3_C2 LEEA Zones 4-5|[93]|0|CDF_FLOAT|7206|
|3_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL3|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL3|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE3|[93]|0|CDF_FLOAT|7206|
|4_C2 LEEA Zones 6-7|[93]|0|CDF_FLOAT|7206|
|4_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL4|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL4|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE4|[93]|0|CDF_FLOAT|7206|
|5_C2 LEEA Zones 8-9|[93]|0|CDF_FLOAT|7206|
|5_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL5|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL5|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE5|[93]|0|CDF_FLOAT|7206|
|6_C2 LEEA Zones 10-11|[93]|0|CDF_FLOAT|7206|
|6_Data Quality|[]|0|CDF_FLOAT|113|
|START_AZIMUTHAL6|[93]|0|CDF_FLOAT|7206|
|STOP_AZIMUTHAL6|[93]|0|CDF_FLOAT|7206|
|PITCH_ANGLE6|[93]|0|CDF_FLOAT|7206|
|MODE0_PEACE Mode|[]|0|CDF_FLOAT|113|
# de_uv_sai_19910218_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|1|
|Time_PB5|[3]|1000|CDF_INT4|1|
|Image_Counts|[121, 150]|1000|CDF_UINT1|1|
|Filter|[2]|1000|CDF_INT4|1|
|AltF|[]|1000|CDF_REAL4|1|
|First_MLC|[]|1000|CDF_INT4|1|
|Last_MLC|[]|1000|CDF_INT4|1|
|OA_time_PB5|[3]|1000|CDF_INT4|1|
|SC_Pos_GCI|[3]|1000|CDF_REAL4|1|
|SC_Vel_GCI|[3]|1000|CDF_REAL4|1|
|SC_SpinV_GCI|[3]|1000|CDF_REAL4|1|
|Sun_Vctr_GCI|[3]|1000|CDF_REAL4|1|
|Orb_Normal_GCI|[3]|1000|CDF_REAL4|1|
|GeoLng_RAs|[121, 150]|1000|CDF_REAL4|1|
|GeoLat_Dec|[121, 150]|1000|CDF_REAL4|1|
|Pixel_Alts|[121, 150]|1000|CDF_REAL4|1|
|Pixel_UTs_PB5|[3, 121, 150]|1000|CDF_INT4|1|
|RGBColorTable|[3, 256]|1|CDF_INT2|1|
|Limit_Lo|[]|1000|CDF_INT2|1|
|Limit_Hi|[]|1000|CDF_INT2|1|
|ExpandedCount|[128]|1|CDF_REAL4|1|
|Intens_Tables|[128, 12]|1|CDF_REAL4|1|
|Image_Header|[101]|1000|CDF_INT4|1|
|Scan_Headers|[12, 121]|1000|CDF_INT2|1|
|label_time|[3]|1|CDF_CHAR|1|
|unit_time|[3]|1|CDF_CHAR|1|
|format_time|[3]|1|CDF_CHAR|1|
|norm_cart|[3]|1|CDF_CHAR|1|
|label_vector|[3]|1|CDF_CHAR|1|
|label_spin_vctr|[3]|1|CDF_CHAR|1|
|label_sun_vctr|[3]|1|CDF_CHAR|1|
|label_orbn_vctr|[3]|1|CDF_CHAR|1|
|image_row|[150]|1|CDF_INT4|1|
|image_column|[121]|1|CDF_INT4|1|
|imhdr_field|[101]|1|CDF_CHAR|1|
|shdr_field|[64]|1|CDF_CHAR|1|
|unit_filter|[2]|1|CDF_CHAR|1|
|label_filter|[2]|1|CDF_CHAR|1|
|format_filter|[2]|1|CDF_CHAR|1|
# ge_k0_cpi_19921231_v02.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[3, 2]|0|CDF_EPOCH|18|
|Time_PB5|[3, 2]|0|CDF_INT4|26|
|SW_P_Den|[3, 2]|0|CDF_REAL4|9|
|SW_P_AVGE|[3, 2]|0|CDF_REAL4|9|
|SW_V|[3, 2]|0|CDF_REAL4|26|
|Quality_SW|[3, 2]|0|CDF_REAL4|9|
|GAP_FLAG|[3, 2]|0|CDF_INT4|9|
|HP_P_Den|[3, 2]|0|CDF_REAL4|9|
|HP_P_AVGE|[3, 2]|0|CDF_REAL4|9|
|HP_V|[3, 2]|0|CDF_REAL4|18|
|HP_E_AVGE|[3, 2]|0|CDF_REAL4|9|
|W|[3, 2]|0|CDF_REAL4|9|
|Quality_HP|[3, 2]|0|CDF_REAL4|9|
|Quality_IC|[3, 2]|0|CDF_REAL4|9|
|H_P_FLAG|[3, 2]|0|CDF_INT1|3|
|HE_PP_FLAG|[3, 2]|0|CDF_INT1|3|
|HE_P_FLAG|[3, 2]|0|CDF_INT1|3|
|O_P_FLAG|[3, 2]|0|CDF_INT1|3|
|label_time|[3, 2]|0|CDF_CHAR|1|
|unit_time|[3, 2]|0|CDF_CHAR|1|
|format_time|[3, 2]|0|CDF_CHAR|1|
|label_v2|[3, 2]|0|CDF_CHAR|1|
|label_v3|[3, 2]|0|CDF_CHAR|1|
|cartesian2|[3, 2]|0|CDF_CHAR|1|
|cartesian3|[3, 2]|0|CDF_CHAR|1|
# i1_av_ott_1983351130734_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|satellite|[]|1|CDF_INT4|1|
|station_id|[]|1|CDF_INT4|1|
|power_code|[]|1|CDF_INT4|1|
|s/r_code|[]|1|CDF_INT4|1|
|pps_code|[]|1|CDF_INT4|1|
|DMODE|[]|1|CDF_INT4|1|
|GMODE|[]|1|CDF_INT4|1|
|mixed_mode|[]|1|CDF_INT4|1|
|fix_freq|[]|1|CDF_INT4|1|
|year|[]|1|CDF_INT4|1|
|doy|[]|1|CDF_INT4|1|
|hr|[]|1|CDF_INT4|1|
|min|[]|1|CDF_INT4|1|
|sec|[]|1|CDF_REAL8|1|
|LMT|[2]|1|CDF_INT4|1|
|label_LMT|[2]|1|CDF_CHAR|1|
|unit_LMT|[2]|1|CDF_CHAR|1|
|geo_coord|[3]|1|CDF_REAL4|1|
|label_geo|[3]|1|CDF_CHAR|1|
|unit_geo|[3]|1|CDF_CHAR|1|
|GMLMT|[2]|1|CDF_INT4|1|
|label_GMLMT|[2]|1|CDF_CHAR|1|
|GMLAT|[]|1|CDF_REAL4|1|
|GMLONG|[]|1|CDF_REAL4|1|
|FH|[]|1|CDF_REAL4|1|
|INV_LAT|[]|1|CDF_REAL4|1|
|DIP|[]|1|CDF_INT4|1|
|CHI|[]|1|CDF_INT4|1|
|L|[]|1|CDF_REAL4|1|
|sun|[]|1|CDF_INT4|1|
|CEP|[]|1|CDF_INT4|1|
|VLF|[]|1|CDF_INT4|1|
|SEA|[]|1|CDF_INT4|1|
|IMS1|[]|1|CDF_INT4|1|
|IMS2|[]|1|CDF_INT4|1|
|SPS|[]|1|CDF_INT4|1|
|EPD|[]|1|CDF_INT4|1|
|swept_start|[]|1|CDF_INT4|1|
|Time_mark|[22]|1|CDF_REAL8|1|
|freq_mark|[22]|1|CDF_REAL8|1|
|vh_num|[]|1|CDF_INT4|1|
|f_num|[]|1|CDF_INT4|1|
|delay_time|[335]|1|CDF_REAL8|1|
|v_height|[335]|1|CDF_REAL8|1|
|Epoch|[]|0|CDF_EPOCH|1|
|ampl|[335]|1000|CDF_UINT1|1|
|freq|[]|1000|CDF_REAL8|1|
# im_k0_euv_20011231_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|1|
|gci_pos|[3]|0|CDF_REAL8|1|
|geo_pos|[3]|0|CDF_REAL8|1|
|gsm_pos|[3]|0|CDF_REAL8|1|
|gci_spinaxis|[3]|0|CDF_REAL8|1|
|IMAGE|[140, 140]|0|CDF_REAL4|1|
|Roll_Angle|[]|0|CDF_REAL4|1|
|cartesian|[3]|0|CDF_CHAR|1|
|Polar_Zone|[140]|0|CDF_CHAR|1|
|Spin_Sect|[140]|0|CDF_CHAR|1|
|metavar0|[3]|0|CDF_CHAR|1|
|metavar1|[3]|0|CDF_CHAR|1|
# im_k0_rpi_20051218_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|3|
|ProgramSpecs|[25]|0|CDF_INT2|18|
|Duration_ms|[]|0|CDF_UINT4|2|
|NadirMET|[]|0|CDF_UINT4|2|
|StartMET|[]|0|CDF_UINT4|2|
|OpMode|[]|0|CDF_UCHAR|5|
|NumDopplers|[]|0|CDF_UINT2|1|
|RepetitionRate|[]|0|CDF_FLOAT|2|
|XmtrAntenna|[]|0|CDF_UCHAR|6|
|Couplers|[]|0|CDF_UCHAR|2|
|Waveform|[]|0|CDF_UCHAR|9|
|BaseGain|[]|0|CDF_UCHAR|7|
|GainControl|[]|0|CDF_UCHAR|4|
|FreqSearch|[]|0|CDF_UCHAR|7|
|PeakPower|[]|0|CDF_INT2|1|
|NumFreqs|[]|0|CDF_INT2|1|
|Frequency|[256]|0|CDF_FLOAT|189|
|NumRanges|[]|0|CDF_UINT1|1|
|Range|[128]|0|CDF_FLOAT|189|
|Amplitude|[256, 128]|0|CDF_UINT1|189|
|MPA|[256]|0|CDF_UINT1|95|
|Azimuth|[256, 128]|0|CDF_UINT1|189|
|Zenith|[256, 128]|0|CDF_UINT1|189|
|DopplerNumber|[256, 128]|0|CDF_UINT1|189|
|DopplerTranslation|[256]|0|CDF_REAL4|189|
# im_k1_rpi_20051217_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|18|
|ProgramSpecs|[25]|0|CDF_INT2|102|
|Duration_ms|[]|0|CDF_UINT4|9|
|NadirMET|[]|0|CDF_UINT4|9|
|StartMET|[]|0|CDF_UINT4|9|
|NumRepetitions|[]|0|CDF_INT2|5|
|BaseGain|[]|0|CDF_UCHAR|39|
|GainControl|[]|0|CDF_UCHAR|20|
|NumFreqs|[]|0|CDF_INT2|5|
|Frequency|[256]|0|CDF_FLOAT|1118|
|Amplitude_X|[256]|0|CDF_FLOAT|1118|
|Amplitude_Y|[256]|0|CDF_FLOAT|1118|
|Amplitude_Z|[256]|0|CDF_FLOAT|1118|
|Amplitude_XY|[256]|0|CDF_FLOAT|1118|
# mms1_fpi_fast_sitl_20150801132440_v0.0.0.cdf
Byte Order: LITTLE_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_TT2000|1|
|mms1_fpi_CIDPside|[]|5120|CDF_INT1|2|
|mms1_fpi_dataQuality|[]|1280|CDF_UINT4|5|
|mms1_fpi_startDelPhi_count|[]|2560|CDF_UINT2|3|
|mms1_fpi_startDelPhi_angle|[]|1280|CDF_REAL4|5|
|mms1_fpi_Nbursts_DES|[]|2560|CDF_INT2|3|
|mms1_fpi_Nbursts_DIS|[]|2560|CDF_INT2|3|
|mms1_fpi_ePseudoContentVar|[]|640|CDF_REAL8|9|
|mms1_fpi_ePseudoContentDelta|[]|1280|CDF_REAL4|5|
|mms1_fpi_ePseudoParaFluxVar|[]|640|CDF_REAL8|9|
|mms1_fpi_ePseudoParaFluxMean|[]|1280|CDF_REAL4|5|
|mms1_fpi_ePseudoDirContentVar|[]|640|CDF_REAL8|9|
|mms1_fpi_ePseudoDirContentMean|[]|1280|CDF_REAL4|5|
|mms1_fpi_iPseudoContentVar|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoContentDelta|[]|1280|CDF_REAL4|5|
|mms1_fpi_iPseudoFluxVar_X_SC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_X_DSC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_Y_SC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_Y_DSC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_Z_SC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_Z_DSC|[]|640|CDF_REAL8|9|
|mms1_fpi_iPseudoFluxVar_Norm|[]|640|CDF_REAL8|9|
|mms1_fpi_ePseudoContent|[335]|4|CDF_REAL4|1400|
|mms1_fpi_ePseudoParaFlux|[335]|4|CDF_REAL4|1400|
|mms1_fpi_ePseudoDirContent|[335]|4|CDF_REAL4|1400|
|mms1_fpi_iPseudoContent|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_X_SC|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_X_DSC|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_Y_SC|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_Y_DSC|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_Z_SC|[68]|19|CDF_REAL4|295|
|mms1_fpi_iPseudoFlux_Z_DSC|[68]|19|CDF_REAL4|295|
|mms1_fpi_DESterm_index|[335]|0|CDF_INT2|1|
|mms1_fpi_DISterm_index|[68]|0|CDF_INT1|1|
|mms1_fpi_ePitchAngDist_lowEn|[30]|43|CDF_REAL4|131|
|mms1_fpi_ePitchAngDist_midEn|[30]|43|CDF_REAL4|131|
|mms1_fpi_ePitchAngDist_highEn|[30]|43|CDF_REAL4|131|
|mms1_fpi_eEnergySpectr_pX|[32]|40|CDF_REAL4|140|
|mms1_fpi_eEnergySpectr_mX|[32]|40|CDF_REAL4|140|
|mms1_fpi_eEnergySpectr_pY|[32]|40|CDF_REAL4|140|
|mms1_fpi_eEnergySpectr_mY|[32]|40|CDF_REAL4|140|
|mms1_fpi_eEnergySpectr_pZ|[32]|40|CDF_REAL4|140|
|mms1_fpi_eEnergySpectr_mZ|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_pX|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_mX|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_pY|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_mY|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_pZ|[32]|40|CDF_REAL4|140|
|mms1_fpi_iEnergySpectr_mZ|[32]|40|CDF_REAL4|140|
|mms1_fpi_pitch_index|[30]|0|CDF_INT1|1|
|mms1_fpi_energy_index|[32]|0|CDF_INT1|1|
|mms1_fpi_bentPipeB_X_SC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_Y_SC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_Z_SC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_Z_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_bentPipeB_Norm|[]|640|CDF_REAL8|9|
|mms1_fpi_DESnumberDensity|[]|1280|CDF_REAL4|5|
|mms1_fpi_eBulkV_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_eBulkV_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_eBulkV_Z_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_eVcrossB_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_eVcrossB_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_eVcrossB_Z_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_XX_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_XY_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_XZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_YY_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_YZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESpress_ZZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESanisotropy|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESagyrotropy|[]|1280|CDF_REAL4|5|
|mms1_fpi_DEStempPara|[]|1280|CDF_REAL4|5|
|mms1_fpi_DEStempPerp|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESmachNumber|[]|1280|CDF_REAL4|5|
|mms1_fpi_DESalfvenSpeed|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISnumberDensity|[]|1280|CDF_REAL4|5|
|mms1_fpi_iBulkV_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_iBulkV_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_iBulkV_Z_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_iVcrossB_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_iVcrossB_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_iVcrossB_Z_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_XX_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_XY_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_XZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_YY_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_YZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISpress_ZZ_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISanisotropy|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISagyrotropy|[]|1280|CDF_REAL4|5|
|mms1_fpi_DIStempPara|[]|1280|CDF_REAL4|5|
|mms1_fpi_DIStempPerp|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISmachNumber|[]|1280|CDF_REAL4|5|
|mms1_fpi_DISalfvenSpeed|[]|1280|CDF_REAL4|5|
|mms1_fpi_FPIplasmaBeta|[]|1280|CDF_REAL4|5|
|mms1_fpi_Jplasma_X_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_Jplasma_Y_DSC|[]|1280|CDF_REAL4|5|
|mms1_fpi_Jplasma_Z_DSC|[]|1280|CDF_REAL4|5|
# po_h4_pwi_19970901_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|DATA_QUALITY|[]|1000|CDF_INT4|447|
|HFWR_Ex2K|[]|1000|CDF_REAL4|447|
|HFWR_Ey2K|[]|1000|CDF_REAL4|447|
|HFWR_Ez2K|[]|1000|CDF_REAL4|447|
|HFWR_Bx2K|[]|1000|CDF_REAL4|447|
|HFWR_By2K|[]|1000|CDF_REAL4|447|
|HFWR_Bz2K|[]|1000|CDF_REAL4|447|
|Epoch0|[]|1000|CDF_EPOCH|1|
|Gain1|[]|1000|CDF_INT4|1|
|Gain2|[]|1000|CDF_INT4|1|
|Gain3|[]|1000|CDF_INT4|1|
|MGain|[]|1000|CDF_INT4|1|
|Epoch|[]|0|CDF_EPOCH|1|
|FilterMode|[]|1|CDF_INT4|1|
|Delta_T|[]|1|CDF_REAL8|1|
|FFT_SIZE|[]|1|CDF_INT4|1|
|Num_Spec|[]|1|CDF_INT4|1|
# po_h9_pwi_1997010103_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[3984]|0|CDF_EPOCH|1|
|Delta_T|[3984]|1000|CDF_REAL8|43|
|Sample_rate|[3984]|1000|CDF_REAL4|43|
|FilterMode|[3984]|1000|CDF_BYTE|43|
|DATA_MODE|[3984]|1000|CDF_BYTE|43|
|WBR_Ant|[3984]|1000|CDF_BYTE|43|
|Gain1|[3984]|1000|CDF_BYTE|43|
|Gain2|[3984]|1000|CDF_BYTE|43|
|Translation|[3984]|1000|CDF_INT4|43|
|NumPoints|[3984]|1000|CDF_INT4|43|
|DATA_QUALITY|[3984]|1000|CDF_BYTE|43|
|WBR_Elec|[3984]|1000|CDF_REAL4|43|
no locator!
|Num_Snap|[3984]|1|CDF_INT4|1|
|FFT_size|[3984]|1|CDF_INT4|1|
|Data_No|[3984]|1|CDF_INT4|1|
# po_k0_uvi_20051230_v02.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[3, 228, 200, 23, 20]|0|CDF_EPOCH|1|
|Time_PB5|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|IMG_MINUS_MSEC|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|
|IMG_PLUS_MSEC|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|
|POST_GAP_FLAG|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|QUALITY_FLAG|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|KPGS_VERSION|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|NOMINAL_OUTPUT_PERIOD|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|SYSTEM|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|SEQ|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|MODE|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|GAIN|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|DOOR|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|GCI_POSITION|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|ATTITUDE|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|GCI_SUN|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|GCI_LOOK_DIR|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|
|DSP_ANGLE|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|
|FILTER|[3, 228, 200, 23, 20]|0|CDF_INT4|1|
|IMAGE_DATA|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|
|GEODETIC_LAT|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|
|GEODETIC_LONG|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|
|label_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|unit_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|format_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|label_GCIpos|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|cartesian|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|
|ptr_row|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|ptr_col|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|row|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
|col|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|
# tha_l2_fgm_20070729_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|tha_fge_ssl|[3]|0|CDF_FLOAT|1|
|tha_fge_dsl|[3]|0|CDF_FLOAT|1|
|tha_fge_gse|[3]|0|CDF_FLOAT|1|
|tha_fge_gsm|[3]|0|CDF_FLOAT|1|
|tha_fge_compno|[3]|0|CDF_INT4|1|
|tha_fge_labl|[3]|0|CDF_CHAR|1|
|tha_fge_time|[]|0|CDF_DOUBLE|1|
|tha_fge_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fgl_ssl|[3]|0|CDF_FLOAT|1|
|tha_fgl_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgl_gse|[3]|0|CDF_FLOAT|1|
|tha_fgl_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgl_compno|[3]|0|CDF_INT4|1|
|tha_fgl_time|[]|0|CDF_DOUBLE|1|
|tha_fgl_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fgh_ssl|[3]|0|CDF_FLOAT|1|
|tha_fgh_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgh_gse|[3]|0|CDF_FLOAT|1|
|tha_fgh_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgh_compno|[3]|0|CDF_INT4|1|
|tha_fgh_time|[]|0|CDF_DOUBLE|1|
|tha_fgh_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fgs_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgs_gse|[3]|0|CDF_FLOAT|1|
|tha_fgs_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgs_compno|[3]|0|CDF_INT4|1|
|tha_fgs_time|[]|0|CDF_DOUBLE|1|
|tha_fgs_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|Rep_xyz|[3]|0|CDF_CHAR|1|
|range_epoch|[]|0|CDF_EPOCH|1|
|tha_fgl_labl|[3]|0|CDF_CHAR|1|
|tha_fgh_labl|[3]|0|CDF_CHAR|1|
|tha_fgs_labl|[3]|0|CDF_CHAR|1|
# tha_l2_fgm_20101202_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|tha_fgs_btotal|[]|0|CDF_FLOAT|1|
|tha_fgs_gse|[3]|0|CDF_FLOAT|1|
|tha_fgs_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgs_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgs_compno|[3]|0|CDF_INT4|1|
|tha_fgs_time|[]|0|CDF_DOUBLE|1|
|tha_fgs_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fgl_btotal|[]|0|CDF_FLOAT|1|
|tha_fgl_gse|[3]|0|CDF_FLOAT|1|
|tha_fgl_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgl_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgl_ssl|[3]|0|CDF_FLOAT|1|
|tha_fgl_compno|[3]|0|CDF_INT4|1|
|tha_fgl_time|[]|0|CDF_DOUBLE|1|
|tha_fgl_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fgh_btotal|[]|0|CDF_FLOAT|1|
|tha_fgh_gse|[3]|0|CDF_FLOAT|1|
|tha_fgh_gsm|[3]|0|CDF_FLOAT|1|
|tha_fgh_dsl|[3]|0|CDF_FLOAT|1|
|tha_fgh_ssl|[3]|0|CDF_FLOAT|1|
|tha_fgh_compno|[3]|0|CDF_INT4|1|
|tha_fgh_time|[]|0|CDF_DOUBLE|1|
|tha_fgh_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|tha_fge_btotal|[]|0|CDF_FLOAT|1|
|tha_fge_gse|[3]|0|CDF_FLOAT|1|
|tha_fge_gsm|[3]|0|CDF_FLOAT|1|
|tha_fge_dsl|[3]|0|CDF_FLOAT|1|
|tha_fge_ssl|[3]|0|CDF_FLOAT|1|
|tha_fge_compno|[3]|0|CDF_INT4|1|
|tha_fge_labl|[3]|0|CDF_CHAR|1|
|tha_fge_time|[]|0|CDF_DOUBLE|1|
|tha_fge_epoch0|[]|0|CDF_EPOCH|1|
no locator!
|Rep_xyz|[3]|0|CDF_CHAR|1|
|range_epoch|[]|0|CDF_EPOCH|1|
|tha_fgl_labl|[3]|0|CDF_CHAR|1|
|tha_fgh_labl|[3]|0|CDF_CHAR|1|
|tha_fgs_labl|[3]|0|CDF_CHAR|1|
# tha_l2_scm_20160831_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
no locator!
|tha_scf_btotal|[]|241664|CDF_FLOAT|1|
|tha_scf_gse|[3]|85333|CDF_FLOAT|3|
|tha_scf_gsm|[3]|85333|CDF_FLOAT|3|
|tha_scf_dsl|[3]|85333|CDF_FLOAT|3|
|tha_scf_compno|[3]|1|CDF_INT4|1|
|tha_scf_time|[]|128000|CDF_DOUBLE|2|
|tha_scf_epoch0|[]|1|CDF_EPOCH|1|
no locator!
|tha_scp_btotal|[]|1024|CDF_FLOAT|1|
|tha_scp_gse|[3]|1024|CDF_FLOAT|1|
|tha_scp_gsm|[3]|1024|CDF_FLOAT|1|
|tha_scp_dsl|[3]|1024|CDF_FLOAT|1|
|tha_scp_compno|[3]|1|CDF_INT4|1|
|tha_scp_time|[]|1024|CDF_DOUBLE|1|
|tha_scp_epoch0|[]|1|CDF_EPOCH|1|
no locator!
no locator!
no locator!
no locator!
no locator!
|tha_scw_compno|[3]|1|CDF_INT4|1|
no locator!
|tha_scw_epoch0|[]|1|CDF_EPOCH|1|
|Rep_xyz|[3]|1|CDF_CHAR|1|
|range_epoch|[]|2|CDF_EPOCH|1|
|tha_scp_labl|[3]|1|CDF_CHAR|1|
|tha_scw_labl|[3]|1|CDF_CHAR|1|
|tha_scf_labl|[3]|1|CDF_CHAR|1|
# timed_L1Cdisk_guvi_20060601005849_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Intensity1_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity2_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity3_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity4_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity5_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity1_AllProfiles|[130]|10|CDF_FLOAT|162|
|Intensity2_AllProfiles|[130]|10|CDF_FLOAT|162|
|Intensity3_AllProfiles|[130]|10|CDF_FLOAT|162|
|Intensity4_AllProfiles|[130]|10|CDF_FLOAT|162|
|Intensity5_AllProfiles|[130]|10|CDF_FLOAT|162|
|Intensity1_SampleProfile|[7]|183|CDF_FLOAT|9|
|Intensity2_SampleProfile|[7]|183|CDF_FLOAT|9|
|Intensity3_SampleProfile|[7]|183|CDF_FLOAT|9|
|Intensity4_SampleProfile|[7]|183|CDF_FLOAT|9|
|Intensity5_SampleProfile|[7]|183|CDF_FLOAT|9|
|orbitNumber|[]|1280|CDF_INT4|1|
|GeographLatMedian|[]|1280|CDF_FLOAT|2|
|GeographLonMedian|[]|1280|CDF_FLOAT|2|
|GeomagLatMedian|[]|1280|CDF_FLOAT|2|
|GeomagLonMedian|[]|1280|CDF_FLOAT|2|
|Detector|[]|5120|CDF_BYTE|1|
|Slit|[]|5120|CDF_BYTE|1|
|GeographLat|[1647, 130]|1|CDF_FLOAT|1|
|GeographLon|[1647, 130]|1|CDF_FLOAT|1|
|GeomagLat|[1647, 130]|1|CDF_FLOAT|1|
|GeomagLon|[1647, 130]|1|CDF_FLOAT|1|
|PiercePointAlt|[1647, 130]|1|CDF_FLOAT|1|
|SolarZenithAngle|[1647, 130]|1|CDF_FLOAT|1|
|DQI|[1647, 130]|1|CDF_BYTE|1|
|DataRegion|[1647, 130]|1|CDF_BYTE|1|
|SystematicError1_rectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError1_rectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError2_rectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError2_rectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError3_rectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError3_rectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError4_rectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError4_rectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError5_rectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError5_rectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity1_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError1_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError1_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity2_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError2_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError2_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity3_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError3_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError3_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity4_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError4_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError4_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|Intensity5_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|SystematicError5_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|StatisticalError5_unrectified|[1647, 130]|1|CDF_FLOAT|1|
|Epoch|[]|0|CDF_EPOCH|1|
|Epoch2|[]|0|CDF_EPOCH|1|
|scan_number|[7]|1|CDF_INT2|1|
|DOY|[1647]|2|CDF_INT2|1|
|Time|[1647]|1|CDF_INT4|1|
|row|[1647]|1|CDF_INT2|1|
|col|[130]|1|CDF_INT2|1|
|int1Profiles|[7]|1|CDF_CHAR|1|
|int2Profiles|[7]|1|CDF_CHAR|1|
|int3Profiles|[7]|1|CDF_CHAR|1|
|int4Profiles|[7]|1|CDF_CHAR|1|
|int5Profiles|[7]|1|CDF_CHAR|1|
# twins1_l1_imager_2010102701_v01.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[]|0|CDF_EPOCH|1|
|satellite|[]|2560|CDF_INT2|1|
|smooth_image|[9, 90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e1|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e2|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e3|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e4|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e5|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e6|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e7|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e8|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_e9|[90, 22]|1|CDF_DOUBLE|65|
|pixel_sweep_count|[90, 22]|1|CDF_DOUBLE|65|
|smooth_image_val|[9]|72|CDF_DOUBLE|1|
|smooth_image_energy_kev|[9]|72|CDF_DOUBLE|1|
|smooth_image_version|[]|214|CDF_CHAR|1|
|smooth_image_units|[9]|34|CDF_CHAR|2|
|lonmin_deg|[]|640|CDF_DOUBLE|1|
|lonmax_deg|[]|640|CDF_DOUBLE|1|
|latmin_deg|[]|640|CDF_DOUBLE|1|
|latmax_deg|[]|640|CDF_DOUBLE|1|
|lat_pixelsize_deg|[]|2560|CDF_INT2|1|
|lon_pixelsize_deg|[]|2560|CDF_INT2|1|
|time_YYMMDD|[2]|320|CDF_EPOCH|1|
|time_MJD|[2]|320|CDF_DOUBLE|1|
|smooth_error_image|[9, 90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e1|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e2|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e3|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e4|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e5|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e6|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e7|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e8|[90, 22]|1|CDF_DOUBLE|65|
|smooth_error_image_e9|[90, 22]|1|CDF_DOUBLE|65|
|no_orbit_data|[]|2560|CDF_INT2|1|
|attitude_delta_deg|[]|640|CDF_DOUBLE|1|
|sc_posv_re_eci|[3]|214|CDF_DOUBLE|1|
|spin_axis_eci|[3]|214|CDF_DOUBLE|1|
|prime_meridian_eci|[3]|214|CDF_DOUBLE|1|
|sun_posv_eci|[3]|214|CDF_DOUBLE|1|
|mag_eci|[3]|214|CDF_DOUBLE|1|
|sc_posv_re_sm|[3]|214|CDF_DOUBLE|1|
|spin_axis_sm|[3]|214|CDF_DOUBLE|1|
|prime_meridian_sm|[3]|214|CDF_DOUBLE|1|
|sun_posv_sm|[3]|214|CDF_DOUBLE|1|
|mag_sm|[3]|214|CDF_DOUBLE|1|
|radial_distance_re|[]|640|CDF_DOUBLE|1|
|latitude_deg|[]|640|CDF_DOUBLE|1|
|lshell_dip|[]|640|CDF_DOUBLE|1|
|mlt|[]|640|CDF_DOUBLE|1|
|energy_kev|[9]|72|CDF_DOUBLE|1|
|all_energies|[]|2560|CDF_INT2|1|
|saveset_version|[]|2560|CDF_INT2|1|
|title|[]|79|CDF_CHAR|1|
|units_of_twins_image|[9]|34|CDF_CHAR|2|
|sw_version|[]|427|CDF_CHAR|1|
|creation_time|[]|214|CDF_CHAR|1|
|twins_image|[9, 90, 22]|1|CDF_DOUBLE|65|
|twins_image_e1|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e2|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e3|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e4|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e5|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e6|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e7|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e8|[90, 22]|1|CDF_DOUBLE|65|
|twins_image_e9|[90, 22]|1|CDF_DOUBLE|65|
|error_image|[9, 90, 22]|1|CDF_DOUBLE|65|
|error_image_e1|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e2|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e3|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e4|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e5|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e6|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e7|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e8|[90, 22]|1|CDF_DOUBLE|65|
|error_image_e9|[90, 22]|1|CDF_DOUBLE|65|
|indexvar9|[9]|1|CDF_INT2|1|
# ulysses.cdf
Byte Order: BIG_ENDIAN
 
|name |record<br>dimensions |blocking |type |locations |
|-----|-----------|---------|-----|----------|
|Epoch|[3]|0|CDF_EPOCH|2104|
|Time_PB5|[3]|0|CDF_INT4|2153|
|Dist_HGI|[3]|0|CDF_REAL4|1052|
|Lat_HGI|[3]|0|CDF_REAL4|1052|
|Long_HGI|[3]|0|CDF_REAL4|1052|
|BR_RTN|[3]|0|CDF_REAL4|1052|
|BT_RTN|[3]|0|CDF_REAL4|1052|
|BN_RTN|[3]|0|CDF_REAL4|1052|
|B_scalar|[3]|0|CDF_REAL4|1052|
|V|[3]|0|CDF_REAL4|1052|
|N|[3]|0|CDF_REAL4|1052|
|Temp|[3]|0|CDF_REAL4|1052|
|label_time|[3]|0|CDF_CHAR|1|
|unit_time|[3]|0|CDF_CHAR|1|
|format_time|[3]|0|CDF_CHAR|1|
# Summary
|Type |Count |
|-----|------|
|CDF_INT1|8|
|CDF_INT2|24|
|CDF_INT4|81|
|CDF_INT8|no examples|
|CDF_UINT1|9|
|CDF_UINT2|2|
|CDF_UINT4|7|
|CDF_REAL4|250|
|CDF_REAL8|35|
|CDF_EPOCH|36|
|CDF_EPOCH16|2|
|CDF_TT2000|1|
|CDF_BYTE|18|
|CDF_FLOAT|136|
|CDF_DOUBLE|77|
|CDF_CHAR|156|
|CDF_UCHAR|9|
