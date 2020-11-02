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
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[2, 3]|0|CDF_EPOCH|16|0|R|
|Time_PB5|[2, 3]|0|CDF_INT4|24|0|R|
|dens_lop|[2, 3]|0|CDF_REAL4|8|0|R|
|vel_lop|[2, 3]|0|CDF_REAL4|24|0|R|
|temp_lop|[2, 3]|0|CDF_REAL4|16|0|R|
|tratio_lop|[2, 3]|0|CDF_REAL4|8|0|R|
|dens_hip|[2, 3]|0|CDF_REAL4|8|0|R|
|vel_hip|[2, 3]|0|CDF_REAL4|24|0|R|
|temp_hip|[2, 3]|0|CDF_REAL4|16|0|R|
|theta_phi_hip|[2, 3]|0|CDF_REAL4|16|0|R|
|tratio_hip|[2, 3]|0|CDF_REAL4|8|0|R|
|dens_e|[2, 3]|0|CDF_REAL4|8|0|R|
|temp_e|[2, 3]|0|CDF_REAL4|16|0|R|
|theta_phi_e|[2, 3]|0|CDF_REAL4|16|0|R|
|tratio_e|[2, 3]|0|CDF_REAL4|8|0|R|
|sc_pot|[2, 3]|0|CDF_REAL4|8|0|R|
|bkgd|[2, 3]|0|CDF_REAL4|8|0|R|
|sc_pos_geo|[2, 3]|0|CDF_REAL4|24|0|R|
no locator!
|sc_pos_mag|[2, 3]|0|CDF_REAL4|24|0|R|
|qual_flag|[2, 3]|0|CDF_INT4|8|0|R|
|gap_flag|[2, 3]|0|CDF_INT4|8|0|R|
|label_time|[2, 3]|0|CDF_CHAR|1|0|R|
|unit_time|[2, 3]|0|CDF_CHAR|1|0|R|
|format_time|[2, 3]|0|CDF_CHAR|1|0|R|
|offset_time|[2, 3]|0|CDF_REAL8|1|0|R|
|label_pos_l|[2, 3]|0|CDF_CHAR|1|0|R|
|unit_pos_l|[2, 3]|0|CDF_CHAR|1|0|R|
|angle_pos_l|[2, 3]|0|CDF_CHAR|1|0|R|
|label_possyn_l|[2, 3]|0|CDF_CHAR|1|0|R|
|unit_possyn_l|[2, 3]|0|CDF_CHAR|1|0|R|
|angle_possyn_l|[2, 3]|0|CDF_CHAR|1|0|R|
|label_pos_m|[2, 3]|0|CDF_CHAR|1|0|R|
|unit_pos_m|[2, 3]|0|CDF_CHAR|1|0|R|
|angle_pos_m|[2, 3]|0|CDF_CHAR|1|0|R|
|label_theta_phi|[2, 3]|0|CDF_CHAR|1|0|R|
|label_vel|[2, 3]|0|CDF_CHAR|1|0|R|
|Cartesian|[2, 3]|0|CDF_CHAR|1|0|R|
|label_temp|[2, 3]|0|CDF_CHAR|1|0|R|
# ac_h2_sis_20101105_v06.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|Time_PB5|[3]|0|CDF_INT4|1|0|Z|
|unit_time|[3]|0|CDF_CHAR|1|0|Z|
|label_time|[3]|0|CDF_CHAR|1|0|Z|
|format_time|[3]|0|CDF_CHAR|1|0|Z|
|flux_He|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_He|[8]|0|CDF_CHAR|1|0|Z|
|flux_C|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_C|[8]|0|CDF_CHAR|1|0|Z|
|flux_N|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_N|[8]|0|CDF_CHAR|1|0|Z|
|flux_O|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_O|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ne|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ne|[8]|0|CDF_CHAR|1|0|Z|
|flux_Na|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Na|[8]|0|CDF_CHAR|1|0|Z|
|flux_Mg|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Mg|[8]|0|CDF_CHAR|1|0|Z|
|flux_Al|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Al|[8]|0|CDF_CHAR|1|0|Z|
|flux_Si|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Si|[8]|0|CDF_CHAR|1|0|Z|
|flux_S|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_S|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ar|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ar|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ca|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ca|[8]|0|CDF_CHAR|1|0|Z|
|flux_Fe|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Fe|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ni|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ni|[8]|0|CDF_CHAR|1|0|Z|
|cnt_He|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_He|[8]|0|CDF_CHAR|1|0|Z|
|cnt_C|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_C|[8]|0|CDF_CHAR|1|0|Z|
|cnt_N|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_N|[8]|0|CDF_CHAR|1|0|Z|
|cnt_O|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_O|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ne|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ne|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Na|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Na|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Mg|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Mg|[8]|0|CDF_CHAR|1|0|Z|
no locator!
|label_ebands_cnt_Al|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Si|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Si|[8]|0|CDF_CHAR|1|0|Z|
|cnt_S|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_S|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ar|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ar|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ca|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ca|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Fe|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Fe|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ni|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ni|[8]|0|CDF_CHAR|1|0|Z|
# ac_or_ssc_20031101_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|XYZ_GSE|[3]|0|CDF_DOUBLE|198|0|Z|
|cartesian|[3]|0|CDF_CHAR|1|0|Z|
|xyz_lbl|[3]|0|CDF_CHAR|1|0|Z|
|Epoch|[]|0|CDF_EPOCH|173|0|R|
|GSE_LAT|[]|0|CDF_FLOAT|87|0|R|
|GSE_LON|[]|0|CDF_FLOAT|87|0|R|
|RADIUS|[]|0|CDF_DOUBLE|173|0|R|
# ac_or_ssc_20040809_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|Time_PB5|[3]|0|CDF_INT4|1|0|Z|
|unit_time|[3]|0|CDF_CHAR|1|0|Z|
|label_time|[3]|0|CDF_CHAR|1|0|Z|
|format_time|[3]|0|CDF_CHAR|1|0|Z|
|flux_He|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_He|[8]|0|CDF_CHAR|1|0|Z|
|flux_C|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_C|[8]|0|CDF_CHAR|1|0|Z|
|flux_N|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_N|[8]|0|CDF_CHAR|1|0|Z|
|flux_O|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_O|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ne|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ne|[8]|0|CDF_CHAR|1|0|Z|
|flux_Na|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Na|[8]|0|CDF_CHAR|1|0|Z|
|flux_Mg|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Mg|[8]|0|CDF_CHAR|1|0|Z|
|flux_Al|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Al|[8]|0|CDF_CHAR|1|0|Z|
|flux_Si|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Si|[8]|0|CDF_CHAR|1|0|Z|
|flux_S|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_S|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ar|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ar|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ca|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ca|[8]|0|CDF_CHAR|1|0|Z|
|flux_Fe|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Fe|[8]|0|CDF_CHAR|1|0|Z|
|flux_Ni|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_flux_Ni|[8]|0|CDF_CHAR|1|0|Z|
|cnt_He|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_He|[8]|0|CDF_CHAR|1|0|Z|
|cnt_C|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_C|[8]|0|CDF_CHAR|1|0|Z|
|cnt_N|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_N|[8]|0|CDF_CHAR|1|0|Z|
|cnt_O|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_O|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ne|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ne|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Na|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Na|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Mg|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Mg|[8]|0|CDF_CHAR|1|0|Z|
no locator!
|label_ebands_cnt_Al|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Si|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Si|[8]|0|CDF_CHAR|1|0|Z|
|cnt_S|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_S|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ar|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ar|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ca|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ca|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Fe|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Fe|[8]|0|CDF_CHAR|1|0|Z|
|cnt_Ni|[8]|0|CDF_REAL4|2|0|Z|
|label_ebands_cnt_Ni|[8]|0|CDF_CHAR|1|0|Z|
# bigcdf_compressed.cdf
Byte Order: LITTLE_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|temp|[1024, 768]|1|CDF_DOUBLE|400|1|Z|
# c1_waveform_wbd_200202080940_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[2]|512000|CDF_EPOCH16|33|1|Z|
|Bandwidth|[]|512000|CDF_REAL4|33|1|Z|
|Translation|[]|512000|CDF_REAL4|33|1|Z|
|Resolution|[]|512000|CDF_BYTE|33|1|Z|
|ANTENNA|[]|512000|CDF_BYTE|33|1|Z|
|Gain|[]|512000|CDF_BYTE|33|1|Z|
|Ant_B_Field_Angle|[]|512000|CDF_REAL4|33|1|Z|
|Ant_Xgse_Angle|[]|512000|CDF_REAL4|33|1|Z|
|Ant_YZgse_Plane_Angle|[]|512000|CDF_REAL4|33|1|Z|
|DC_Offset|[]|512000|CDF_REAL4|33|1|Z|
|WBD_Elec|[]|512000|CDF_REAL4|33|1|Z|
|WBD_Mag|[]|512000|CDF_REAL4|33|1|Z|
|DATA_QUALITY|[]|512000|CDF_BYTE|33|1|Z|
# c1_waveform_wbd_200202080940_v01_subset.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[2]|512000|CDF_EPOCH16|1|1|Z|
|Bandwidth|[]|512000|CDF_REAL4|1|1|Z|
|Translation|[]|512000|CDF_REAL4|1|1|Z|
|Resolution|[]|512000|CDF_BYTE|1|1|Z|
|ANTENNA|[]|512000|CDF_BYTE|1|1|Z|
|Gain|[]|512000|CDF_BYTE|1|1|Z|
|Ant_B_Field_Angle|[]|512000|CDF_REAL4|1|1|Z|
|Ant_Xgse_Angle|[]|512000|CDF_REAL4|1|1|Z|
|Ant_YZgse_Plane_Angle|[]|512000|CDF_REAL4|1|1|Z|
|DC_Offset|[]|512000|CDF_REAL4|1|1|Z|
|WBD_Elec|[]|512000|CDF_REAL4|1|1|Z|
|WBD_Mag|[]|512000|CDF_REAL4|1|1|Z|
|DATA_QUALITY|[]|512000|CDF_BYTE|1|1|Z|
# cl_jp_pgp_20031001_v52.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|L_gse_xyz|[3]|0|CDF_CHAR|1|0|Z|
|Half_interval__CL_JP_PGP|[]|0|CDF_REAL8|1|0|Z|
|Epoch__CL_JP_PGP|[]|0|CDF_EPOCH|1|0|Z|
|sc_orbit_num__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_r_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|L_sc_r_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|sc_v_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|L_sc_v_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|sc_dr1_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|sc_dr2_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|sc_dr3_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|sc_dr4_xyz_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|L_sc1_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|L_sc2_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|L_sc3_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|L_sc4_dr_xyz_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|sc_at1_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at1_long__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at2_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at2_long__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at3_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at3_long__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at4_lat__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_at4_long__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_config_QG__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_config_QR__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_dr_min__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_dr_max__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|gse_gsm__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|dipole_tilt__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_geom_size__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_geom_elong__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_geom_planarity__CL_JP_PGP|[]|0|CDF_REAL4|1|0|Z|
|sc_geom_E_dir_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|L_geom_E_dir_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
|sc_geom_P_nor_gse__CL_JP_PGP|[3]|0|CDF_REAL4|1|0|Z|
|L_geom_P_nor_gse__CL_JP_PGP|[3]|0|CDF_CHAR|1|0|Z|
# cl_sp_edi_00000000_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|L_gse_xyz|[3]|0|CDF_CHAR|1|0|Z|
|Half_interval__CL_SP_EDI|[]|0|CDF_REAL8|1|0|Z|
no locator!
|Status__CL_SP_EDI|[7]|0|CDF_UINT1|1|0|Z|
|L_Status_EDI_SP|[7]|0|CDF_CHAR|1|0|Z|
no locator!
|L_V_ed_xyz_gse__CL_SP_EDI|[3]|0|CDF_CHAR|1|0|Z|
# cluster-2_cp3drl_2002052000000_v1.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|226|0|Z|
|Epoch_Start|[]|0|CDF_REAL8|1|0|Z|
|Epoch_End|[]|0|CDF_REAL8|226|0|Z|
|Mode_Epoch|[]|0|CDF_EPOCH|226|0|Z|
|Mode_Epoch_Start|[]|0|CDF_REAL8|1|0|Z|
|Mode_Epoch_End|[]|0|CDF_REAL8|226|0|Z|
|Center_Scan|[93]|0|CDF_FLOAT|1|0|Z|
|Band_Low_Scan|[93]|0|CDF_FLOAT|1|0|Z|
|Band_High_Scan|[93]|0|CDF_FLOAT|1|0|Z|
|1_C2 LEEA Zones 0-1|[93]|0|CDF_FLOAT|7206|0|Z|
|1_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL1|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL1|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE1|[93]|0|CDF_FLOAT|7206|0|Z|
|2_C2 LEEA Zones 2-3|[93]|0|CDF_FLOAT|7206|0|Z|
|2_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL2|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL2|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE2|[93]|0|CDF_FLOAT|7206|0|Z|
|3_C2 LEEA Zones 4-5|[93]|0|CDF_FLOAT|7206|0|Z|
|3_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL3|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL3|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE3|[93]|0|CDF_FLOAT|7206|0|Z|
|4_C2 LEEA Zones 6-7|[93]|0|CDF_FLOAT|7206|0|Z|
|4_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL4|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL4|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE4|[93]|0|CDF_FLOAT|7206|0|Z|
|5_C2 LEEA Zones 8-9|[93]|0|CDF_FLOAT|7206|0|Z|
|5_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL5|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL5|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE5|[93]|0|CDF_FLOAT|7206|0|Z|
|6_C2 LEEA Zones 10-11|[93]|0|CDF_FLOAT|7206|0|Z|
|6_Data Quality|[]|0|CDF_FLOAT|113|0|Z|
|START_AZIMUTHAL6|[93]|0|CDF_FLOAT|7206|0|Z|
|STOP_AZIMUTHAL6|[93]|0|CDF_FLOAT|7206|0|Z|
|PITCH_ANGLE6|[93]|0|CDF_FLOAT|7206|0|Z|
|MODE0_PEACE Mode|[]|0|CDF_FLOAT|113|0|Z|
# de_uv_sai_19910218_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|Time_PB5|[3]|1000|CDF_INT4|1|1|Z|
|Image_Counts|[121, 150]|1000|CDF_UINT1|1|1|Z|
|Filter|[2]|1000|CDF_INT4|1|1|Z|
|AltF|[]|1000|CDF_REAL4|1|1|Z|
|First_MLC|[]|1000|CDF_INT4|1|1|Z|
|Last_MLC|[]|1000|CDF_INT4|1|1|Z|
|OA_time_PB5|[3]|1000|CDF_INT4|1|1|Z|
|SC_Pos_GCI|[3]|1000|CDF_REAL4|1|1|Z|
|SC_Vel_GCI|[3]|1000|CDF_REAL4|1|1|Z|
|SC_SpinV_GCI|[3]|1000|CDF_REAL4|1|1|Z|
|Sun_Vctr_GCI|[3]|1000|CDF_REAL4|1|1|Z|
|Orb_Normal_GCI|[3]|1000|CDF_REAL4|1|1|Z|
|GeoLng_RAs|[121, 150]|1000|CDF_REAL4|1|1|Z|
|GeoLat_Dec|[121, 150]|1000|CDF_REAL4|1|1|Z|
|Pixel_Alts|[121, 150]|1000|CDF_REAL4|1|1|Z|
|Pixel_UTs_PB5|[3, 121, 150]|1000|CDF_INT4|1|1|Z|
|RGBColorTable|[3, 256]|1|CDF_INT2|1|1|Z|
|Limit_Lo|[]|1000|CDF_INT2|1|1|Z|
|Limit_Hi|[]|1000|CDF_INT2|1|1|Z|
|ExpandedCount|[128]|1|CDF_REAL4|1|1|Z|
|Intens_Tables|[128, 12]|1|CDF_REAL4|1|1|Z|
|Image_Header|[101]|1000|CDF_INT4|1|1|Z|
|Scan_Headers|[12, 121]|1000|CDF_INT2|1|1|Z|
|label_time|[3]|1|CDF_CHAR|1|1|Z|
|unit_time|[3]|1|CDF_CHAR|1|1|Z|
|format_time|[3]|1|CDF_CHAR|1|1|Z|
|norm_cart|[3]|1|CDF_CHAR|1|1|Z|
|label_vector|[3]|1|CDF_CHAR|1|1|Z|
|label_spin_vctr|[3]|1|CDF_CHAR|1|1|Z|
|label_sun_vctr|[3]|1|CDF_CHAR|1|1|Z|
|label_orbn_vctr|[3]|1|CDF_CHAR|1|1|Z|
|image_row|[150]|1|CDF_INT4|1|1|Z|
|image_column|[121]|1|CDF_INT4|1|1|Z|
|imhdr_field|[101]|1|CDF_CHAR|1|1|Z|
|shdr_field|[64]|1|CDF_CHAR|1|1|Z|
|unit_filter|[2]|1|CDF_CHAR|1|1|Z|
|label_filter|[2]|1|CDF_CHAR|1|1|Z|
|format_filter|[2]|1|CDF_CHAR|1|1|Z|
# ge_k0_cpi_19921231_v02.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[3, 2]|0|CDF_EPOCH|18|0|R|
|Time_PB5|[3, 2]|0|CDF_INT4|26|0|R|
|SW_P_Den|[3, 2]|0|CDF_REAL4|9|0|R|
|SW_P_AVGE|[3, 2]|0|CDF_REAL4|9|0|R|
|SW_V|[3, 2]|0|CDF_REAL4|26|0|R|
|Quality_SW|[3, 2]|0|CDF_REAL4|9|0|R|
|GAP_FLAG|[3, 2]|0|CDF_INT4|9|0|R|
|HP_P_Den|[3, 2]|0|CDF_REAL4|9|0|R|
|HP_P_AVGE|[3, 2]|0|CDF_REAL4|9|0|R|
|HP_V|[3, 2]|0|CDF_REAL4|18|0|R|
|HP_E_AVGE|[3, 2]|0|CDF_REAL4|9|0|R|
|W|[3, 2]|0|CDF_REAL4|9|0|R|
|Quality_HP|[3, 2]|0|CDF_REAL4|9|0|R|
|Quality_IC|[3, 2]|0|CDF_REAL4|9|0|R|
|H_P_FLAG|[3, 2]|0|CDF_INT1|3|0|R|
|HE_PP_FLAG|[3, 2]|0|CDF_INT1|3|0|R|
|HE_P_FLAG|[3, 2]|0|CDF_INT1|3|0|R|
|O_P_FLAG|[3, 2]|0|CDF_INT1|3|0|R|
|label_time|[3, 2]|0|CDF_CHAR|1|0|R|
|unit_time|[3, 2]|0|CDF_CHAR|1|0|R|
|format_time|[3, 2]|0|CDF_CHAR|1|0|R|
|label_v2|[3, 2]|0|CDF_CHAR|1|0|R|
|label_v3|[3, 2]|0|CDF_CHAR|1|0|R|
|cartesian2|[3, 2]|0|CDF_CHAR|1|0|R|
|cartesian3|[3, 2]|0|CDF_CHAR|1|0|R|
# i1_av_ott_1983351130734_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|satellite|[]|1|CDF_INT4|1|1|Z|
|station_id|[]|1|CDF_INT4|1|1|Z|
|power_code|[]|1|CDF_INT4|1|1|Z|
|s/r_code|[]|1|CDF_INT4|1|1|Z|
|pps_code|[]|1|CDF_INT4|1|1|Z|
|DMODE|[]|1|CDF_INT4|1|1|Z|
|GMODE|[]|1|CDF_INT4|1|1|Z|
|mixed_mode|[]|1|CDF_INT4|1|1|Z|
|fix_freq|[]|1|CDF_INT4|1|1|Z|
|year|[]|1|CDF_INT4|1|1|Z|
|doy|[]|1|CDF_INT4|1|1|Z|
|hr|[]|1|CDF_INT4|1|1|Z|
|min|[]|1|CDF_INT4|1|1|Z|
|sec|[]|1|CDF_REAL8|1|1|Z|
|LMT|[2]|1|CDF_INT4|1|1|Z|
|label_LMT|[2]|1|CDF_CHAR|1|1|Z|
|unit_LMT|[2]|1|CDF_CHAR|1|1|Z|
|geo_coord|[3]|1|CDF_REAL4|1|1|Z|
|label_geo|[3]|1|CDF_CHAR|1|1|Z|
|unit_geo|[3]|1|CDF_CHAR|1|1|Z|
|GMLMT|[2]|1|CDF_INT4|1|1|Z|
|label_GMLMT|[2]|1|CDF_CHAR|1|1|Z|
|GMLAT|[]|1|CDF_REAL4|1|1|Z|
|GMLONG|[]|1|CDF_REAL4|1|1|Z|
|FH|[]|1|CDF_REAL4|1|1|Z|
|INV_LAT|[]|1|CDF_REAL4|1|1|Z|
|DIP|[]|1|CDF_INT4|1|1|Z|
|CHI|[]|1|CDF_INT4|1|1|Z|
|L|[]|1|CDF_REAL4|1|1|Z|
|sun|[]|1|CDF_INT4|1|1|Z|
|CEP|[]|1|CDF_INT4|1|1|Z|
|VLF|[]|1|CDF_INT4|1|1|Z|
|SEA|[]|1|CDF_INT4|1|1|Z|
|IMS1|[]|1|CDF_INT4|1|1|Z|
|IMS2|[]|1|CDF_INT4|1|1|Z|
|SPS|[]|1|CDF_INT4|1|1|Z|
|EPD|[]|1|CDF_INT4|1|1|Z|
|swept_start|[]|1|CDF_INT4|1|1|Z|
|Time_mark|[22]|1|CDF_REAL8|1|1|Z|
|freq_mark|[22]|1|CDF_REAL8|1|1|Z|
|vh_num|[]|1|CDF_INT4|1|1|Z|
|f_num|[]|1|CDF_INT4|1|1|Z|
|delay_time|[335]|1|CDF_REAL8|1|1|Z|
|v_height|[335]|1|CDF_REAL8|1|1|Z|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|ampl|[335]|1000|CDF_UINT1|1|1|Z|
|freq|[]|1000|CDF_REAL8|1|1|Z|
# im_k0_euv_20011231_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|gci_pos|[3]|0|CDF_REAL8|1|0|Z|
|geo_pos|[3]|0|CDF_REAL8|1|0|Z|
|gsm_pos|[3]|0|CDF_REAL8|1|0|Z|
|gci_spinaxis|[3]|0|CDF_REAL8|1|0|Z|
|IMAGE|[140, 140]|0|CDF_REAL4|1|0|Z|
|Roll_Angle|[]|0|CDF_REAL4|1|0|Z|
|cartesian|[3]|0|CDF_CHAR|1|0|Z|
|Polar_Zone|[140]|0|CDF_CHAR|1|0|Z|
|Spin_Sect|[140]|0|CDF_CHAR|1|0|Z|
|metavar0|[3]|0|CDF_CHAR|1|0|Z|
|metavar1|[3]|0|CDF_CHAR|1|0|Z|
# im_k0_rpi_20051218_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|3|0|Z|
|ProgramSpecs|[25]|0|CDF_INT2|18|0|Z|
|Duration_ms|[]|0|CDF_UINT4|2|0|Z|
|NadirMET|[]|0|CDF_UINT4|2|0|Z|
|StartMET|[]|0|CDF_UINT4|2|0|Z|
|OpMode|[]|0|CDF_UCHAR|5|0|Z|
|NumDopplers|[]|0|CDF_UINT2|1|0|Z|
|RepetitionRate|[]|0|CDF_FLOAT|2|0|Z|
|XmtrAntenna|[]|0|CDF_UCHAR|6|0|Z|
|Couplers|[]|0|CDF_UCHAR|2|0|Z|
|Waveform|[]|0|CDF_UCHAR|9|0|Z|
|BaseGain|[]|0|CDF_UCHAR|7|0|Z|
|GainControl|[]|0|CDF_UCHAR|4|0|Z|
|FreqSearch|[]|0|CDF_UCHAR|7|0|Z|
|PeakPower|[]|0|CDF_INT2|1|0|Z|
|NumFreqs|[]|0|CDF_INT2|1|0|Z|
|Frequency|[256]|0|CDF_FLOAT|189|0|Z|
|NumRanges|[]|0|CDF_UINT1|1|0|Z|
|Range|[128]|0|CDF_FLOAT|189|0|Z|
|Amplitude|[256, 128]|0|CDF_UINT1|189|0|Z|
|MPA|[256]|0|CDF_UINT1|95|0|Z|
|Azimuth|[256, 128]|0|CDF_UINT1|189|0|Z|
|Zenith|[256, 128]|0|CDF_UINT1|189|0|Z|
|DopplerNumber|[256, 128]|0|CDF_UINT1|189|0|Z|
|DopplerTranslation|[256]|0|CDF_REAL4|189|0|Z|
# im_k1_rpi_20051217_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|18|0|Z|
|ProgramSpecs|[25]|0|CDF_INT2|102|0|Z|
|Duration_ms|[]|0|CDF_UINT4|9|0|Z|
|NadirMET|[]|0|CDF_UINT4|9|0|Z|
|StartMET|[]|0|CDF_UINT4|9|0|Z|
|NumRepetitions|[]|0|CDF_INT2|5|0|Z|
|BaseGain|[]|0|CDF_UCHAR|39|0|Z|
|GainControl|[]|0|CDF_UCHAR|20|0|Z|
|NumFreqs|[]|0|CDF_INT2|5|0|Z|
|Frequency|[256]|0|CDF_FLOAT|1118|0|Z|
|Amplitude_X|[256]|0|CDF_FLOAT|1118|0|Z|
|Amplitude_Y|[256]|0|CDF_FLOAT|1118|0|Z|
|Amplitude_Z|[256]|0|CDF_FLOAT|1118|0|Z|
|Amplitude_XY|[256]|0|CDF_FLOAT|1118|0|Z|
# mms1_fpi_fast_sitl_20150801132440_v0.0.0.cdf
Byte Order: LITTLE_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_TT2000|1|0|Z|
|mms1_fpi_CIDPside|[]|5120|CDF_INT1|2|1|Z|
|mms1_fpi_dataQuality|[]|1280|CDF_UINT4|5|1|Z|
|mms1_fpi_startDelPhi_count|[]|2560|CDF_UINT2|3|1|Z|
|mms1_fpi_startDelPhi_angle|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_Nbursts_DES|[]|2560|CDF_INT2|3|1|Z|
|mms1_fpi_Nbursts_DIS|[]|2560|CDF_INT2|3|1|Z|
|mms1_fpi_ePseudoContentVar|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_ePseudoContentDelta|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_ePseudoParaFluxVar|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_ePseudoParaFluxMean|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_ePseudoDirContentVar|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_ePseudoDirContentMean|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iPseudoContentVar|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoContentDelta|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iPseudoFluxVar_X_SC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_X_DSC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_Y_SC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_Y_DSC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_Z_SC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_Z_DSC|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_iPseudoFluxVar_Norm|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_ePseudoContent|[335]|4|CDF_REAL4|1400|1|Z|
|mms1_fpi_ePseudoParaFlux|[335]|4|CDF_REAL4|1400|1|Z|
|mms1_fpi_ePseudoDirContent|[335]|4|CDF_REAL4|1400|1|Z|
|mms1_fpi_iPseudoContent|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_X_SC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_X_DSC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_Y_SC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_Y_DSC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_Z_SC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_iPseudoFlux_Z_DSC|[68]|19|CDF_REAL4|295|1|Z|
|mms1_fpi_DESterm_index|[335]|0|CDF_INT2|1|0|Z|
|mms1_fpi_DISterm_index|[68]|0|CDF_INT1|1|0|Z|
|mms1_fpi_ePitchAngDist_lowEn|[30]|43|CDF_REAL4|131|1|Z|
|mms1_fpi_ePitchAngDist_midEn|[30]|43|CDF_REAL4|131|1|Z|
|mms1_fpi_ePitchAngDist_highEn|[30]|43|CDF_REAL4|131|1|Z|
|mms1_fpi_eEnergySpectr_pX|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_eEnergySpectr_mX|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_eEnergySpectr_pY|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_eEnergySpectr_mY|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_eEnergySpectr_pZ|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_eEnergySpectr_mZ|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_pX|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_mX|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_pY|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_mY|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_pZ|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_iEnergySpectr_mZ|[32]|40|CDF_REAL4|140|1|Z|
|mms1_fpi_pitch_index|[30]|0|CDF_INT1|1|0|Z|
|mms1_fpi_energy_index|[32]|0|CDF_INT1|1|0|Z|
|mms1_fpi_bentPipeB_X_SC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_Y_SC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_Z_SC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_bentPipeB_Norm|[]|640|CDF_REAL8|9|1|Z|
|mms1_fpi_DESnumberDensity|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eBulkV_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eBulkV_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eBulkV_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eVcrossB_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eVcrossB_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_eVcrossB_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_XX_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_XY_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_XZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_YY_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_YZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESpress_ZZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESanisotropy|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESagyrotropy|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DEStempPara|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DEStempPerp|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESmachNumber|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DESalfvenSpeed|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISnumberDensity|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iBulkV_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iBulkV_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iBulkV_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iVcrossB_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iVcrossB_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_iVcrossB_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_XX_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_XY_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_XZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_YY_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_YZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISpress_ZZ_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISanisotropy|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISagyrotropy|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DIStempPara|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DIStempPerp|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISmachNumber|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_DISalfvenSpeed|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_FPIplasmaBeta|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_Jplasma_X_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_Jplasma_Y_DSC|[]|1280|CDF_REAL4|5|1|Z|
|mms1_fpi_Jplasma_Z_DSC|[]|1280|CDF_REAL4|5|1|Z|
# po_h4_pwi_19970901_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|DATA_QUALITY|[]|1000|CDF_INT4|447|1|Z|
|HFWR_Ex2K|[]|1000|CDF_REAL4|447|1|Z|
|HFWR_Ey2K|[]|1000|CDF_REAL4|447|1|Z|
|HFWR_Ez2K|[]|1000|CDF_REAL4|447|1|Z|
|HFWR_Bx2K|[]|1000|CDF_REAL4|447|1|Z|
|HFWR_By2K|[]|1000|CDF_REAL4|447|1|Z|
|HFWR_Bz2K|[]|1000|CDF_REAL4|447|1|Z|
|Epoch0|[]|1000|CDF_EPOCH|1|1|Z|
|Gain1|[]|1000|CDF_INT4|1|1|Z|
|Gain2|[]|1000|CDF_INT4|1|1|Z|
|Gain3|[]|1000|CDF_INT4|1|1|Z|
|MGain|[]|1000|CDF_INT4|1|1|Z|
|Epoch|[]|0|CDF_EPOCH|1|0|R|
|FilterMode|[]|1|CDF_INT4|1|1|R|
|Delta_T|[]|1|CDF_REAL8|1|1|R|
|FFT_SIZE|[]|1|CDF_INT4|1|1|R|
|Num_Spec|[]|1|CDF_INT4|1|1|R|
# po_h9_pwi_1997010103_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[3984]|0|CDF_EPOCH|1|0|R|
|Delta_T|[3984]|1000|CDF_REAL8|43|1|R|
|Sample_rate|[3984]|1000|CDF_REAL4|43|1|R|
|FilterMode|[3984]|1000|CDF_BYTE|43|1|R|
|DATA_MODE|[3984]|1000|CDF_BYTE|43|1|R|
|WBR_Ant|[3984]|1000|CDF_BYTE|43|1|R|
|Gain1|[3984]|1000|CDF_BYTE|43|1|R|
|Gain2|[3984]|1000|CDF_BYTE|43|1|R|
|Translation|[3984]|1000|CDF_INT4|43|1|R|
|NumPoints|[3984]|1000|CDF_INT4|43|1|R|
|DATA_QUALITY|[3984]|1000|CDF_BYTE|43|1|R|
|WBR_Elec|[3984]|1000|CDF_REAL4|43|1|R|
no locator!
|Num_Snap|[3984]|1|CDF_INT4|1|1|R|
|FFT_size|[3984]|1|CDF_INT4|1|1|R|
|Data_No|[3984]|1|CDF_INT4|1|1|R|
# po_k0_uvi_20051230_v02.cdf
Byte Order: BIG_ENDIAN<br>
Majority: column<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[3, 228, 200, 23, 20]|0|CDF_EPOCH|1|0|R|
|Time_PB5|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|IMG_MINUS_MSEC|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|0|R|
|IMG_PLUS_MSEC|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|0|R|
|POST_GAP_FLAG|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|QUALITY_FLAG|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|KPGS_VERSION|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|NOMINAL_OUTPUT_PERIOD|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|SYSTEM|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|SEQ|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|MODE|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|GAIN|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|DOOR|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|GCI_POSITION|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|ATTITUDE|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|GCI_SUN|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|GCI_LOOK_DIR|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|0|R|
|DSP_ANGLE|[3, 228, 200, 23, 20]|0|CDF_REAL8|1|0|R|
|FILTER|[3, 228, 200, 23, 20]|0|CDF_INT4|1|0|R|
|IMAGE_DATA|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|0|R|
|GEODETIC_LAT|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|0|R|
|GEODETIC_LONG|[3, 228, 200, 23, 20]|0|CDF_REAL4|8|0|R|
|label_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|unit_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|format_time|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|label_GCIpos|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|cartesian|[3, 228, 200, 23, 20]|0|CDF_CHAR|1|0|R|
|ptr_row|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|ptr_col|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|row|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
|col|[3, 228, 200, 23, 20]|0|CDF_REAL4|1|0|R|
# tha_l2_fgm_20070729_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|tha_fge_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fge_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fge_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fge_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fgl_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgl_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgl_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fgh_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgh_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgh_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fgs_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgs_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgs_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|Rep_xyz|[3]|0|CDF_CHAR|1|0|Z|
|range_epoch|[]|0|CDF_EPOCH|1|0|Z|
|tha_fgl_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fgh_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fgs_labl|[3]|0|CDF_CHAR|1|0|Z|
# tha_l2_fgm_20101202_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|tha_fgs_btotal|[]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgs_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgs_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgs_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fgl_btotal|[]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgl_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgl_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgl_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fgh_btotal|[]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fgh_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fgh_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fgh_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|tha_fge_btotal|[]|0|CDF_FLOAT|1|0|Z|
|tha_fge_gse|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_gsm|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_dsl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_ssl|[3]|0|CDF_FLOAT|1|0|Z|
|tha_fge_compno|[3]|0|CDF_INT4|1|0|Z|
|tha_fge_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fge_time|[]|0|CDF_DOUBLE|1|0|Z|
|tha_fge_epoch0|[]|0|CDF_EPOCH|1|0|Z|
no locator!
|Rep_xyz|[3]|0|CDF_CHAR|1|0|Z|
|range_epoch|[]|0|CDF_EPOCH|1|0|Z|
|tha_fgl_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fgh_labl|[3]|0|CDF_CHAR|1|0|Z|
|tha_fgs_labl|[3]|0|CDF_CHAR|1|0|Z|
# tha_l2_scm_20160831_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
no locator!
|tha_scf_btotal|[]|241664|CDF_FLOAT|1|1|Z|
|tha_scf_gse|[3]|85333|CDF_FLOAT|3|1|Z|
|tha_scf_gsm|[3]|85333|CDF_FLOAT|3|1|Z|
|tha_scf_dsl|[3]|85333|CDF_FLOAT|3|1|Z|
|tha_scf_compno|[3]|1|CDF_INT4|1|0|Z|
|tha_scf_time|[]|128000|CDF_DOUBLE|2|1|Z|
|tha_scf_epoch0|[]|1|CDF_EPOCH|1|0|Z|
no locator!
|tha_scp_btotal|[]|1024|CDF_FLOAT|1|1|Z|
|tha_scp_gse|[3]|1024|CDF_FLOAT|1|1|Z|
|tha_scp_gsm|[3]|1024|CDF_FLOAT|1|1|Z|
|tha_scp_dsl|[3]|1024|CDF_FLOAT|1|1|Z|
|tha_scp_compno|[3]|1|CDF_INT4|1|0|Z|
|tha_scp_time|[]|1024|CDF_DOUBLE|1|1|Z|
|tha_scp_epoch0|[]|1|CDF_EPOCH|1|0|Z|
no locator!
no locator!
no locator!
no locator!
no locator!
|tha_scw_compno|[3]|1|CDF_INT4|1|0|Z|
no locator!
|tha_scw_epoch0|[]|1|CDF_EPOCH|1|0|Z|
|Rep_xyz|[3]|1|CDF_CHAR|1|0|Z|
|range_epoch|[]|2|CDF_EPOCH|1|0|Z|
|tha_scp_labl|[3]|1|CDF_CHAR|1|0|Z|
|tha_scw_labl|[3]|1|CDF_CHAR|1|0|Z|
|tha_scf_labl|[3]|1|CDF_CHAR|1|0|Z|
# timed_L1Cdisk_guvi_20060601005849_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Intensity1_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity2_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity3_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity4_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity5_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity1_AllProfiles|[130]|10|CDF_FLOAT|162|1|Z|
|Intensity2_AllProfiles|[130]|10|CDF_FLOAT|162|1|Z|
|Intensity3_AllProfiles|[130]|10|CDF_FLOAT|162|1|Z|
|Intensity4_AllProfiles|[130]|10|CDF_FLOAT|162|1|Z|
|Intensity5_AllProfiles|[130]|10|CDF_FLOAT|162|1|Z|
|Intensity1_SampleProfile|[7]|183|CDF_FLOAT|9|1|Z|
|Intensity2_SampleProfile|[7]|183|CDF_FLOAT|9|1|Z|
|Intensity3_SampleProfile|[7]|183|CDF_FLOAT|9|1|Z|
|Intensity4_SampleProfile|[7]|183|CDF_FLOAT|9|1|Z|
|Intensity5_SampleProfile|[7]|183|CDF_FLOAT|9|1|Z|
|orbitNumber|[]|1280|CDF_INT4|1|1|Z|
|GeographLatMedian|[]|1280|CDF_FLOAT|2|1|Z|
|GeographLonMedian|[]|1280|CDF_FLOAT|2|1|Z|
|GeomagLatMedian|[]|1280|CDF_FLOAT|2|1|Z|
|GeomagLonMedian|[]|1280|CDF_FLOAT|2|1|Z|
|Detector|[]|5120|CDF_BYTE|1|1|Z|
|Slit|[]|5120|CDF_BYTE|1|1|Z|
|GeographLat|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|GeographLon|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|GeomagLat|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|GeomagLon|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|PiercePointAlt|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SolarZenithAngle|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|DQI|[1647, 130]|1|CDF_BYTE|1|1|Z|
|DataRegion|[1647, 130]|1|CDF_BYTE|1|1|Z|
|SystematicError1_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError1_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError2_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError2_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError3_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError3_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError4_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError4_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError5_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError5_rectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity1_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError1_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError1_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity2_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError2_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError2_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity3_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError3_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError3_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity4_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError4_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError4_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Intensity5_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|SystematicError5_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|StatisticalError5_unrectified|[1647, 130]|1|CDF_FLOAT|1|1|Z|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|Epoch2|[]|0|CDF_EPOCH|1|0|Z|
|scan_number|[7]|1|CDF_INT2|1|1|Z|
|DOY|[1647]|2|CDF_INT2|1|1|Z|
|Time|[1647]|1|CDF_INT4|1|1|Z|
|row|[1647]|1|CDF_INT2|1|1|Z|
|col|[130]|1|CDF_INT2|1|1|Z|
|int1Profiles|[7]|1|CDF_CHAR|1|1|Z|
|int2Profiles|[7]|1|CDF_CHAR|1|1|Z|
|int3Profiles|[7]|1|CDF_CHAR|1|1|Z|
|int4Profiles|[7]|1|CDF_CHAR|1|1|Z|
|int5Profiles|[7]|1|CDF_CHAR|1|1|Z|
# twins1_l1_imager_2010102701_v01.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[]|0|CDF_EPOCH|1|0|Z|
|satellite|[]|2560|CDF_INT2|1|1|Z|
|smooth_image|[9, 90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e1|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e2|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e3|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e4|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e5|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e6|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e7|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e8|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_e9|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|pixel_sweep_count|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_image_val|[9]|72|CDF_DOUBLE|1|1|Z|
|smooth_image_energy_kev|[9]|72|CDF_DOUBLE|1|1|Z|
|smooth_image_version|[]|214|CDF_CHAR|1|1|Z|
|smooth_image_units|[9]|34|CDF_CHAR|2|1|Z|
|lonmin_deg|[]|640|CDF_DOUBLE|1|1|Z|
|lonmax_deg|[]|640|CDF_DOUBLE|1|1|Z|
|latmin_deg|[]|640|CDF_DOUBLE|1|1|Z|
|latmax_deg|[]|640|CDF_DOUBLE|1|1|Z|
|lat_pixelsize_deg|[]|2560|CDF_INT2|1|1|Z|
|lon_pixelsize_deg|[]|2560|CDF_INT2|1|1|Z|
|time_YYMMDD|[2]|320|CDF_EPOCH|1|1|Z|
|time_MJD|[2]|320|CDF_DOUBLE|1|1|Z|
|smooth_error_image|[9, 90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e1|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e2|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e3|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e4|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e5|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e6|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e7|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e8|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|smooth_error_image_e9|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|no_orbit_data|[]|2560|CDF_INT2|1|1|Z|
|attitude_delta_deg|[]|640|CDF_DOUBLE|1|1|Z|
|sc_posv_re_eci|[3]|214|CDF_DOUBLE|1|1|Z|
|spin_axis_eci|[3]|214|CDF_DOUBLE|1|1|Z|
|prime_meridian_eci|[3]|214|CDF_DOUBLE|1|1|Z|
|sun_posv_eci|[3]|214|CDF_DOUBLE|1|1|Z|
|mag_eci|[3]|214|CDF_DOUBLE|1|1|Z|
|sc_posv_re_sm|[3]|214|CDF_DOUBLE|1|1|Z|
|spin_axis_sm|[3]|214|CDF_DOUBLE|1|1|Z|
|prime_meridian_sm|[3]|214|CDF_DOUBLE|1|1|Z|
|sun_posv_sm|[3]|214|CDF_DOUBLE|1|1|Z|
|mag_sm|[3]|214|CDF_DOUBLE|1|1|Z|
|radial_distance_re|[]|640|CDF_DOUBLE|1|1|Z|
|latitude_deg|[]|640|CDF_DOUBLE|1|1|Z|
|lshell_dip|[]|640|CDF_DOUBLE|1|1|Z|
|mlt|[]|640|CDF_DOUBLE|1|1|Z|
|energy_kev|[9]|72|CDF_DOUBLE|1|1|Z|
|all_energies|[]|2560|CDF_INT2|1|1|Z|
|saveset_version|[]|2560|CDF_INT2|1|1|Z|
|title|[]|79|CDF_CHAR|1|1|Z|
|units_of_twins_image|[9]|34|CDF_CHAR|2|1|Z|
|sw_version|[]|427|CDF_CHAR|1|1|Z|
|creation_time|[]|214|CDF_CHAR|1|1|Z|
|twins_image|[9, 90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e1|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e2|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e3|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e4|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e5|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e6|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e7|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e8|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|twins_image_e9|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image|[9, 90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e1|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e2|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e3|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e4|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e5|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e6|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e7|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e8|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|error_image_e9|[90, 22]|1|CDF_DOUBLE|65|1|Z|
|indexvar9|[9]|1|CDF_INT2|1|1|Z|
# ulysses.cdf
Byte Order: BIG_ENDIAN<br>
Majority: row<br>
 
|name |record<br>dimensions |blocking<br>factor |type |locations |compressed |type |
|-----|-----------|---------|-----|----------|-----|---|
|Epoch|[3]|0|CDF_EPOCH|2104|0|R|
|Time_PB5|[3]|0|CDF_INT4|2153|0|R|
|Dist_HGI|[3]|0|CDF_REAL4|1052|0|R|
|Lat_HGI|[3]|0|CDF_REAL4|1052|0|R|
|Long_HGI|[3]|0|CDF_REAL4|1052|0|R|
|BR_RTN|[3]|0|CDF_REAL4|1052|0|R|
|BT_RTN|[3]|0|CDF_REAL4|1052|0|R|
|BN_RTN|[3]|0|CDF_REAL4|1052|0|R|
|B_scalar|[3]|0|CDF_REAL4|1052|0|R|
|V|[3]|0|CDF_REAL4|1052|0|R|
|N|[3]|0|CDF_REAL4|1052|0|R|
|Temp|[3]|0|CDF_REAL4|1052|0|R|
|label_time|[3]|0|CDF_CHAR|1|0|R|
|unit_time|[3]|0|CDF_CHAR|1|0|R|
|format_time|[3]|0|CDF_CHAR|1|0|R|
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
