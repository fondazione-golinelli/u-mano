{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 1,
			"revision" : 0,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 112.0, 77.0, 1774.0, 969.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 113.800000000000011, 358.5, 123.0, 22.0 ],
					"style" : "default",
					"text" : "receive hand_release"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-25",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 113.800000000000011, 289.66227263212204, 116.0, 22.0 ],
					"style" : "default",
					"text" : "receive hand_attack"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 1017.914356989018415, 185.688174366950989, 22.0 ],
					"text" : "route /umano/onehand/release"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 1053.556610451024426, 185.193551659584045, 22.0 ],
					"text" : "send hand_release"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1582.921988058090164, 20.0, 80.0, 22.0 ],
					"style" : "default",
					"text" : "receive beats"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 1196.125624299048468, 67.0, 22.0 ],
					"text" : "send beats"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 1160.483370837042457, 156.0, 22.0 ],
					"text" : "route /umano/onehand/beat"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1380.0, 97.16227263212204, 93.0, 22.0 ],
					"text" : "receive bigbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 1124.841117375036447, 81.0, 22.0 ],
					"text" : "send bigbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 1089.198863913030436, 184.806451797485352, 22.0 ],
					"text" : "route /umano/onehand/bang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-326",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 703.500023961066859, 47.16227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-327",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 666.850023961066995, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-328",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 608.250023961067086, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-323",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 848.500023961066859, 47.16227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-324",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 811.850023961066995, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-325",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 753.250023961067086, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-320",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1137.500023961066972, 47.16227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-321",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1100.850023961067109, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-322",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1042.2500239610672, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-317",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 996.649999999999864, 47.16227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-318",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.0, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-319",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 901.400000000000091, 97.16227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-314",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1138.999999999999773, 263.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-315",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1102.349999999999909, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-316",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1043.75, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-311",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 996.649999999999864, 263.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-312",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.0, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-313",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 901.400000000000091, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-308",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 848.500023961067086, 263.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-309",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 811.850023961067222, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-310",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 753.250023961067313, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-305",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 703.500023961066859, 263.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-306",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 666.850023961066995, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-307",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 608.250023961067086, 313.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-302",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 704.999999999999886, 469.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-303",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 668.350000000000023, 519.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-304",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 609.750000000000114, 519.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-299",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 849.999999999999886, 469.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-300",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 813.350000000000023, 519.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-301",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 754.750000000000114, 519.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-296",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 996.649999999999864, 468.83772736787796, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-297",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.0, 518.83772736787796, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-298",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 901.400000000000091, 518.83772736787796, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-293",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1138.999999999999773, 468.83772736787796, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-294",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1102.349999999999909, 518.83772736787796, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-295",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1043.75, 518.83772736787796, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-290",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1138.999999999999773, 679.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-291",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1102.349999999999909, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-292",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1043.75, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-287",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 996.649999999999864, 679.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-288",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.0, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-289",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 901.400000000000091, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-284",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 850.0, 679.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-285",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 813.350000000000136, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-286",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 754.750000000000227, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-281",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 704.999999999999886, 679.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-282",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 668.350000000000023, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-283",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 609.750000000000114, 729.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-278",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1138.999999999999773, 889.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-279",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1102.349999999999909, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-280",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1043.75, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-275",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 996.649999999999864, 889.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-276",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.0, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-277",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 901.399999999999977, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-272",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 850.0, 889.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-273",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 813.350000000000136, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-274",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 754.750000000000114, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-271",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 705.0, 889.66227263212204, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-269",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 668.350000000000136, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-267",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 609.750000000000114, 939.66227263212204, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-255",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1410.0, 146.0, 150.0, 20.0 ],
					"text" : "all together"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-253",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1380.0, 142.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-251",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1230.0, 984.5, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-249",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1230.0, 780.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-247",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1230.0, 563.83772736787796, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-245",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1230.0, 358.5, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-227",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.0, 1033.0, 128.0, 23.0 ],
					"text" : "#20 little_04",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-228",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1043.75, 963.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-229",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 1043.75, 915.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.427450980392157, 0.843137254901961, 1.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-230",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.0, 900.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-231",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 1033.0, 128.0, 23.0 ],
					"text" : "#19 little_03",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-232",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 901.750000000000114, 963.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-233",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 901.750000000000114, 915.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[1]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.427450980392157, 0.843137254901961, 1.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-234",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 900.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-235",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 1033.0, 128.0, 23.0 ],
					"text" : "#18 little_02",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-236",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 754.750000000000114, 963.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-237",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 754.750000000000114, 915.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[2]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.427450980392157, 0.843137254901961, 1.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-238",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 900.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-239",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 1033.0, 128.0, 23.0 ],
					"text" : "#17 little_01",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-240",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 609.750000000000114, 963.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-241",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 609.750000000000114, 915.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[3]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.427450980392157, 0.843137254901961, 1.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-242",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 900.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-187",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.000000000000227, 823.0, 128.0, 23.0 ],
					"text" : "#16 ring_04",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-188",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1043.750000000000227, 753.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-189",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 1043.750000000000227, 705.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[4]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.345098039215686, 0.298039215686275, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-190",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.000000000000227, 690.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-191",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 823.0, 128.0, 23.0 ],
					"text" : "#15 ring_03",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-192",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 901.750000000000114, 753.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-193",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 901.750000000000114, 705.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[5]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.345098039215686, 0.298039215686275, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-194",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 690.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-195",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 823.0, 128.0, 23.0 ],
					"text" : "#14 ring_02",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-196",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 754.750000000000114, 753.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-197",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 754.750000000000114, 705.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[6]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.345098039215686, 0.298039215686275, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-198",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 690.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-199",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 823.0, 128.0, 23.0 ],
					"text" : "#13 ring_01",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-200",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 609.750000000000114, 753.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-201",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 609.750000000000114, 705.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[7]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.345098039215686, 0.298039215686275, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-202",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 690.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-167",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.000000000000227, 612.33772736787796, 128.0, 23.0 ],
					"text" : "#12 middle_04",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-168",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1043.750000000000227, 542.83772736787796, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-169",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 1043.750000000000227, 495.0, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[8]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.392156862745098, 0.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-170",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.000000000000227, 479.33772736787796, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-171",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 612.33772736787796, 128.0, 23.0 ],
					"text" : "#11 middle_03",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-172",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 901.750000000000114, 542.83772736787796, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-173",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 901.750000000000114, 495.0, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[9]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.392156862745098, 0.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-174",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 479.33772736787796, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-175",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 612.33772736787796, 128.0, 23.0 ],
					"text" : "#10 middle_02",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-176",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 754.750000000000114, 542.83772736787796, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-177",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 754.750000000000114, 495.0, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[10]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.392156862745098, 0.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-178",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 479.33772736787796, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-179",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 612.33772736787796, 128.0, 23.0 ],
					"text" : "#9 middle_01",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-180",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 609.750000000000114, 542.83772736787796, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-181",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 609.750000000000114, 495.0, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[11]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.392156862745098, 0.0, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-182",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 479.33772736787796, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-147",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.0, 407.0, 128.0, 23.0 ],
					"text" : "#8 index_04",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-148",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1043.75, 337.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-149",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 1043.75, 289.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[12]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.0, 0.854901960784314, 0.282352941176471, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-150",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1034.0, 274.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-151",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 407.0, 128.0, 23.0 ],
					"text" : "#7 index_03",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-152",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 901.750000000000114, 337.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-153",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 901.750000000000114, 289.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[13]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.0, 0.854901960784314, 0.282352941176471, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-154",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 892.0, 274.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-155",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 407.0, 128.0, 23.0 ],
					"text" : "#6 index_02",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-156",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 754.750000000000114, 337.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-157",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 754.750000000000114, 289.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[14]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.0, 0.854901960784314, 0.282352941176471, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-158",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 745.0, 274.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-159",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 407.0, 128.0, 23.0 ],
					"text" : "#5 index_01",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-160",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 609.750000000000114, 337.5, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-161",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 609.750000000000114, 289.66227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[15]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.0, 0.854901960784314, 0.282352941176471, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-162",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 600.0, 274.0, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-135",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1032.5000239610672, 190.5, 128.0, 23.0 ],
					"text" : "#4 thumb_04",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-136",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1042.2500239610672, 121.0, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-137",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 1042.2500239610672, 73.16227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[16]"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-131",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 890.500023961066972, 190.5, 128.0, 23.0 ],
					"text" : "#3 thumb_03",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-132",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 900.250023961067086, 121.0, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-133",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 900.250023961067086, 73.16227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[17]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-134",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 890.500023961066972, 57.5, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-127",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 743.500023961066972, 190.5, 128.0, 23.0 ],
					"text" : "#2 thumb_02",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-128",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 753.250023961067086, 121.0, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-129",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 753.250023961067086, 73.16227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[18]"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-130",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 743.500023961066972, 57.5, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-108",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 246.0, 625.8495689069523, 32.0, 22.0 ],
					"text" : "print"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-107",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 946.629850065006394, 186.0, 22.0 ],
					"text" : "route /umano/onehand/attack"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-106",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 875.345343140994373, 186.0, 22.0 ],
					"text" : "route /umano/onehand/hand/amp"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-105",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 804.060836216982352, 185.688174366950989, 22.0 ],
					"text" : "route /umano/onehand/hand/freq"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-103",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 768.418582754976342, 187.0, 22.0 ],
					"text" : "send durer_amplitudes"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-104",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 732.776329292970331, 187.0, 22.0 ],
					"text" : "route /umano/onehand/durer/amp"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-102",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 697.134075830964321, 187.0, 22.0 ],
					"text" : "send durer_frequencies"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-98",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 75.0, 661.49182236895831, 187.0, 22.0 ],
					"text" : "route /umano/onehand/durer/freq"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-97",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 75.0, 590.207315444946289, 97.0, 22.0 ],
					"text" : "udpreceive 8888"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 115.800000000000011, 208.0, 142.0, 22.0 ],
					"style" : "default",
					"text" : "receive hand_amplitudes"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 116.0, 80.0, 143.0, 22.0 ],
					"style" : "default",
					"text" : "receive durer_amplitudes"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 115.800000000000011, 143.0, 146.0, 22.0 ],
					"style" : "default",
					"text" : "receive hand_frequencies"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 116.0, 20.0, 147.0, 22.0 ],
					"style" : "default",
					"text" : "receive durer_frequencies"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-81",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 598.500023961066972, 190.5, 128.0, 23.0 ],
					"text" : "#1 thumb_01",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"gridcolor" : [ 0.176470588235294, 0.168627450980392, 0.168627450980392, 1.0 ],
					"id" : "obj-76",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 608.250023961067086, 121.0, 108.600000000000023, 66.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-77",
					"maxclass" : "newobj",
					"numinlets" : 9,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "", "" ],
					"patching_rect" : [ 608.250023961067086, 73.16227263212204, 108.5, 22.0 ],
					"text" : "phalanx~",
					"varname" : "phalanx~[19]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-68",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1230.0, 135.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-59",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 982.272103527012405, 186.0, 22.0 ],
					"text" : "send hand_attack"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-49",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 910.987596603000384, 186.0, 22.0 ],
					"text" : "send hand_amplitudes"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 839.703089678988363, 185.688174366950989, 22.0 ],
					"text" : "send hand_frequencies"
				}

			}
, 			{
				"box" : 				{
					"calccount" : 70,
					"id" : "obj-5",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1630.0, 635.5, 305.0, 184.0 ],
					"style" : "default",
					"triglevel" : 0.01
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 1551.0, 540.0, 47.0, 22.0 ],
					"style" : "default",
					"text" : "*~ 0.05"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"interpinlet" : 1,
					"maxclass" : "gain~",
					"multichannelvariant" : 0,
					"numinlets" : 2,
					"numoutlets" : 2,
					"orientation" : 2,
					"outlettype" : [ "signal", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1560.0, 612.33772736787796, 19.0, 111.0 ],
					"style" : "default"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1470.0, 775.5, 33.0, 22.0 ],
					"style" : "default",
					"text" : "stop"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1467.0, 706.5, 74.0, 22.0 ],
					"style" : "default",
					"text" : "startwindow"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1551.0, 743.5, 37.0, 22.0 ],
					"style" : "default",
					"text" : "dac~"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-124",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 598.500023961066972, 57.5, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"bordercolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-138",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1032.5000239610672, 57.5, 128.0, 156.0 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 116.0, 50.0, 341.0, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 113.800000000000011, 390.5, 340.999999999999943, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-26",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 113.800000000000011, 321.66227263212204, 340.999999999999943, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 1582.921988058090164, 52.0, 314.0, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 115.800000000000011, 239.0, 314.0, 22.0 ],
					"style" : "default",
					"text" : "unpack 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-21",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 116.0, 109.0, 341.0, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float", "float" ],
					"patching_rect" : [ 115.800000000000011, 175.0, 340.999999999999943, 22.0 ],
					"style" : "default",
					"text" : "unpack 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 6 ],
					"midpoints" : [ 1607.94830384756392, 84.0, 1173.0, 84.0, 1173.0, 33.0, 829.875023961067086, 33.0 ],
					"source" : [ "obj-10", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 6 ],
					"midpoints" : [ 1623.474619637037449, 84.0, 1173.0, 84.0, 1173.0, 33.0, 976.875023961067086, 33.0 ],
					"source" : [ "obj-10", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 6 ],
					"midpoints" : [ 1639.000935426511205, 84.0, 1173.0, 84.0, 1173.0, 33.0, 1118.8750239610672, 33.0 ],
					"source" : [ "obj-10", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 6 ],
					"midpoints" : [ 1701.106198584406002, 249.0, 1120.375, 249.0 ],
					"source" : [ "obj-10", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 6 ],
					"midpoints" : [ 1685.579882794932246, 249.0, 978.375000000000114, 249.0 ],
					"source" : [ "obj-10", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 6 ],
					"midpoints" : [ 1670.05356700545849, 249.0, 831.375000000000114, 249.0 ],
					"source" : [ "obj-10", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 6 ],
					"midpoints" : [ 1654.527251215984961, 249.0, 686.375000000000114, 249.0 ],
					"source" : [ "obj-10", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 6 ],
					"midpoints" : [ 1763.211461742300799, 435.0, 1173.0, 435.0, 1173.0, 453.0, 1120.375000000000227, 453.0 ],
					"source" : [ "obj-10", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 6 ],
					"midpoints" : [ 1747.685145952827042, 435.0, 1173.0, 435.0, 1173.0, 453.0, 978.375000000000114, 453.0 ],
					"source" : [ "obj-10", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 6 ],
					"midpoints" : [ 1732.158830163353286, 435.0, 1173.0, 435.0, 1173.0, 453.0, 831.375000000000114, 453.0 ],
					"source" : [ "obj-10", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 6 ],
					"midpoints" : [ 1716.63251437387953, 435.0, 1173.0, 435.0, 1173.0, 453.0, 686.375000000000114, 453.0 ],
					"source" : [ "obj-10", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 6 ],
					"midpoints" : [ 1825.316724900195368, 435.0, 1173.0, 435.0, 1173.0, 666.0, 1120.375000000000227, 666.0 ],
					"source" : [ "obj-10", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 6 ],
					"midpoints" : [ 1809.790409110721839, 435.0, 1173.0, 435.0, 1173.0, 666.0, 978.375000000000114, 666.0 ],
					"source" : [ "obj-10", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 6 ],
					"midpoints" : [ 1794.264093321248083, 435.0, 1173.0, 435.0, 1173.0, 666.0, 831.375000000000114, 666.0 ],
					"source" : [ "obj-10", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 6 ],
					"midpoints" : [ 1778.737777531774327, 435.0, 1173.0, 435.0, 1173.0, 666.0, 686.375000000000114, 666.0 ],
					"source" : [ "obj-10", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 6 ],
					"midpoints" : [ 1887.421988058090164, 494.33113631606102, 1120.375, 494.33113631606102 ],
					"source" : [ "obj-10", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 6 ],
					"midpoints" : [ 1871.895672268616408, 494.33113631606102, 978.375000000000114, 494.33113631606102 ],
					"source" : [ "obj-10", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 6 ],
					"midpoints" : [ 1856.36935647914288, 494.33113631606102, 831.375000000000114, 494.33113631606102 ],
					"source" : [ "obj-10", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 6 ],
					"midpoints" : [ 1840.843040689669124, 494.33113631606102, 686.375000000000114, 494.33113631606102 ],
					"source" : [ "obj-10", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 6 ],
					"midpoints" : [ 1592.421988058090164, 75.0, 1173.0, 75.0, 1173.0, 33.0, 684.875023961067086, 33.0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-103", 0 ],
					"midpoints" : [ 84.5, 756.0, 84.5, 756.0 ],
					"source" : [ "obj-104", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"midpoints" : [ 84.5, 828.0, 84.5, 828.0 ],
					"source" : [ "obj-105", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-49", 0 ],
					"midpoints" : [ 84.5, 900.0, 84.5, 900.0 ],
					"source" : [ "obj-106", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-59", 0 ],
					"midpoints" : [ 84.5, 969.0, 84.5, 969.0 ],
					"source" : [ "obj-107", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"midpoints" : [ 125.300000000000011, 168.0, 125.300000000000011, 168.0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 1479.5, 807.0, 1536.0, 807.0, 1536.0, 738.0, 1560.5, 738.0 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-128", 0 ],
					"midpoints" : [ 762.750023961067086, 96.0, 762.750023961067086, 96.0 ],
					"order" : 1,
					"source" : [ "obj-129", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-324", 0 ],
					"midpoints" : [ 852.250023961067086, 96.0, 873.0, 96.0, 873.0, 33.0, 821.350023961066995, 33.0 ],
					"source" : [ "obj-129", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-325", 0 ],
					"midpoints" : [ 807.500023961067086, 60.0, 750.0, 60.0, 750.0, 93.0, 762.750023961067086, 93.0 ],
					"source" : [ "obj-129", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 762.750023961067086, 96.0, 738.0, 96.0, 738.0, 249.0, 1560.5, 249.0 ],
					"order" : 0,
					"source" : [ "obj-129", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 1476.5, 738.0, 1560.5, 738.0 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-132", 0 ],
					"midpoints" : [ 909.750023961067086, 96.0, 909.750023961067086, 96.0 ],
					"order" : 1,
					"source" : [ "obj-133", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-318", 0 ],
					"midpoints" : [ 999.250023961067086, 96.0, 969.5, 96.0 ],
					"source" : [ "obj-133", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-319", 0 ],
					"midpoints" : [ 954.500023961067086, 60.0, 897.0, 60.0, 897.0, 93.0, 910.900000000000091, 93.0 ],
					"source" : [ "obj-133", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 909.750023961067086, 96.0, 885.0, 96.0, 885.0, 249.0, 1560.5, 249.0 ],
					"order" : 0,
					"source" : [ "obj-133", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-136", 0 ],
					"midpoints" : [ 1051.7500239610672, 96.0, 1051.7500239610672, 96.0 ],
					"order" : 1,
					"source" : [ "obj-137", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-321", 0 ],
					"midpoints" : [ 1141.2500239610672, 96.0, 1110.350023961067109, 96.0 ],
					"source" : [ "obj-137", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-322", 0 ],
					"midpoints" : [ 1096.5000239610672, 60.0, 1038.0, 60.0, 1038.0, 93.0, 1051.7500239610672, 93.0 ],
					"source" : [ "obj-137", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 1051.7500239610672, 96.0, 1029.0, 96.0, 1029.0, 249.0, 1560.5, 249.0 ],
					"order" : 0,
					"source" : [ "obj-137", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-148", 0 ],
					"midpoints" : [ 1053.25, 312.0, 1053.25, 312.0 ],
					"order" : 1,
					"source" : [ "obj-149", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-315", 0 ],
					"midpoints" : [ 1142.75, 312.0, 1111.849999999999909, 312.0 ],
					"source" : [ "obj-149", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-316", 0 ],
					"midpoints" : [ 1098.0, 312.0, 1053.25, 312.0 ],
					"source" : [ "obj-149", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 1053.25, 312.0, 1029.0, 312.0, 1029.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-149", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 1 ],
					"midpoints" : [ 1567.5, 729.0, 1578.5, 729.0 ],
					"order" : 1,
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 1567.5, 729.0, 1560.5, 729.0 ],
					"order" : 2,
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"midpoints" : [ 1567.5, 714.0, 1617.0, 714.0, 1617.0, 630.0, 1639.5, 630.0 ],
					"order" : 0,
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-152", 0 ],
					"midpoints" : [ 911.250000000000114, 312.0, 911.250000000000114, 312.0 ],
					"order" : 1,
					"source" : [ "obj-153", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-312", 0 ],
					"midpoints" : [ 1000.750000000000114, 312.0, 969.5, 312.0 ],
					"source" : [ "obj-153", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-313", 0 ],
					"midpoints" : [ 956.000000000000114, 276.0, 888.0, 276.0, 888.0, 309.0, 910.900000000000091, 309.0 ],
					"source" : [ "obj-153", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 911.250000000000114, 312.0, 888.0, 312.0, 888.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-153", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-156", 0 ],
					"midpoints" : [ 764.250000000000114, 312.0, 764.250000000000114, 312.0 ],
					"order" : 1,
					"source" : [ "obj-157", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-309", 0 ],
					"midpoints" : [ 853.750000000000114, 312.0, 873.0, 312.0, 873.0, 249.0, 821.350023961067222, 249.0 ],
					"source" : [ "obj-157", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-310", 0 ],
					"midpoints" : [ 809.000000000000114, 276.0, 750.0, 276.0, 750.0, 309.0, 762.750023961067313, 309.0 ],
					"source" : [ "obj-157", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 764.250000000000114, 312.0, 738.0, 312.0, 738.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-157", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 2 ],
					"midpoints" : [ 142.247368421052641, 198.0, 102.0, 198.0, 102.0, 6.0, 785.125023961067086, 6.0 ],
					"source" : [ "obj-16", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 2 ],
					"midpoints" : [ 159.194736842105272, 198.0, 102.0, 198.0, 102.0, 6.0, 932.125023961067086, 6.0 ],
					"source" : [ "obj-16", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 2 ],
					"midpoints" : [ 176.142105263157902, 198.0, 102.0, 198.0, 102.0, 6.0, 1074.1250239610672, 6.0 ],
					"source" : [ "obj-16", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 2 ],
					"midpoints" : [ 243.931578947368394, 204.0, 267.0, 204.0, 267.0, 225.0, 1075.625, 225.0 ],
					"source" : [ "obj-16", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 2 ],
					"midpoints" : [ 226.984210526315792, 204.0, 267.0, 204.0, 267.0, 225.0, 933.625000000000114, 225.0 ],
					"source" : [ "obj-16", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 2 ],
					"midpoints" : [ 210.036842105263162, 204.0, 267.0, 204.0, 267.0, 225.0, 786.625000000000114, 225.0 ],
					"source" : [ "obj-16", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 2 ],
					"midpoints" : [ 193.089473684210532, 204.0, 267.0, 204.0, 267.0, 225.0, 641.625000000000114, 225.0 ],
					"source" : [ "obj-16", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 2 ],
					"midpoints" : [ 311.721052631578914, 225.0, 585.0, 225.0, 585.0, 453.0, 1075.625000000000227, 453.0 ],
					"source" : [ "obj-16", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 2 ],
					"midpoints" : [ 294.773684210526312, 225.0, 585.0, 225.0, 585.0, 456.0, 933.625000000000114, 456.0 ],
					"source" : [ "obj-16", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 2 ],
					"midpoints" : [ 277.826315789473711, 225.0, 585.0, 225.0, 585.0, 456.0, 786.625000000000114, 456.0 ],
					"source" : [ "obj-16", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 2 ],
					"midpoints" : [ 260.878947368421052, 207.0, 585.0, 207.0, 585.0, 480.0, 641.625000000000114, 480.0 ],
					"source" : [ "obj-16", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 2 ],
					"midpoints" : [ 379.510526315789434, 225.0, 585.0, 225.0, 585.0, 666.0, 1075.625000000000227, 666.0 ],
					"source" : [ "obj-16", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 2 ],
					"midpoints" : [ 362.563157894736833, 225.0, 585.0, 225.0, 585.0, 666.0, 933.625000000000114, 666.0 ],
					"source" : [ "obj-16", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 2 ],
					"midpoints" : [ 345.615789473684174, 225.0, 585.0, 225.0, 585.0, 666.0, 786.625000000000114, 666.0 ],
					"source" : [ "obj-16", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 2 ],
					"midpoints" : [ 328.668421052631516, 225.0, 585.0, 225.0, 585.0, 690.0, 641.625000000000114, 690.0 ],
					"source" : [ "obj-16", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 2 ],
					"midpoints" : [ 447.299999999999955, 306.0, 585.0, 306.0, 585.0, 876.0, 1075.625, 876.0 ],
					"source" : [ "obj-16", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 2 ],
					"midpoints" : [ 430.352631578947353, 225.0, 585.0, 225.0, 585.0, 876.0, 933.625000000000114, 876.0 ],
					"source" : [ "obj-16", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 2 ],
					"midpoints" : [ 413.405263157894694, 225.0, 585.0, 225.0, 585.0, 876.0, 786.625000000000114, 876.0 ],
					"source" : [ "obj-16", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 2 ],
					"midpoints" : [ 396.457894736842093, 225.0, 585.0, 225.0, 585.0, 900.0, 641.625000000000114, 900.0 ],
					"source" : [ "obj-16", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 2 ],
					"midpoints" : [ 125.300000000000011, 198.0, 102.0, 198.0, 102.0, 6.0, 640.125023961067086, 6.0 ],
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-160", 0 ],
					"midpoints" : [ 619.250000000000114, 312.0, 619.250000000000114, 312.0 ],
					"order" : 1,
					"source" : [ "obj-161", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-306", 0 ],
					"midpoints" : [ 708.750000000000114, 312.0, 729.0, 312.0, 729.0, 249.0, 676.350023961066995, 249.0 ],
					"source" : [ "obj-161", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-307", 0 ],
					"midpoints" : [ 664.000000000000114, 276.0, 606.0, 276.0, 606.0, 309.0, 617.750023961067086, 309.0 ],
					"source" : [ "obj-161", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 619.250000000000114, 312.0, 585.0, 312.0, 585.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-161", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-168", 0 ],
					"midpoints" : [ 1053.250000000000227, 519.0, 1053.250000000000227, 519.0 ],
					"order" : 1,
					"source" : [ "obj-169", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-294", 0 ],
					"midpoints" : [ 1142.750000000000227, 519.0, 1152.0, 519.0, 1152.0, 492.0, 1111.849999999999909, 492.0 ],
					"source" : [ "obj-169", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-295", 0 ],
					"midpoints" : [ 1098.000000000000227, 480.0, 1038.0, 480.0, 1038.0, 513.0, 1053.25, 513.0 ],
					"source" : [ "obj-169", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 1053.250000000000227, 519.0, 1038.0, 519.0, 1038.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-169", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-172", 0 ],
					"midpoints" : [ 911.250000000000114, 519.0, 911.250000000000114, 519.0 ],
					"order" : 1,
					"source" : [ "obj-173", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-297", 0 ],
					"midpoints" : [ 1000.750000000000114, 519.0, 1011.0, 519.0, 1011.0, 492.0, 969.5, 492.0 ],
					"source" : [ "obj-173", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-298", 0 ],
					"midpoints" : [ 956.000000000000114, 480.0, 888.0, 480.0, 888.0, 513.0, 910.900000000000091, 513.0 ],
					"source" : [ "obj-173", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 911.250000000000114, 519.0, 888.0, 519.0, 888.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-173", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-176", 0 ],
					"midpoints" : [ 764.250000000000114, 519.0, 764.250000000000114, 519.0 ],
					"order" : 1,
					"source" : [ "obj-177", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-300", 0 ],
					"midpoints" : [ 853.750000000000114, 519.0, 873.0, 519.0, 873.0, 456.0, 822.850000000000023, 456.0 ],
					"source" : [ "obj-177", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-301", 0 ],
					"midpoints" : [ 809.000000000000114, 480.0, 741.0, 480.0, 741.0, 513.0, 764.250000000000114, 513.0 ],
					"source" : [ "obj-177", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 764.250000000000114, 519.0, 741.0, 519.0, 741.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-177", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-180", 0 ],
					"midpoints" : [ 619.250000000000114, 519.0, 619.250000000000114, 519.0 ],
					"order" : 1,
					"source" : [ "obj-181", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-303", 0 ],
					"midpoints" : [ 708.750000000000114, 519.0, 729.0, 519.0, 729.0, 456.0, 677.850000000000023, 456.0 ],
					"source" : [ "obj-181", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-304", 0 ],
					"midpoints" : [ 664.000000000000114, 480.0, 606.0, 480.0, 606.0, 513.0, 619.250000000000114, 513.0 ],
					"source" : [ "obj-181", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 619.250000000000114, 519.0, 594.0, 519.0, 594.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-181", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-188", 0 ],
					"midpoints" : [ 1053.250000000000227, 729.0, 1053.250000000000227, 729.0 ],
					"order" : 1,
					"source" : [ "obj-189", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-291", 0 ],
					"midpoints" : [ 1142.750000000000227, 729.0, 1173.0, 729.0, 1173.0, 666.0, 1111.849999999999909, 666.0 ],
					"source" : [ "obj-189", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-292", 0 ],
					"midpoints" : [ 1098.000000000000227, 690.0, 1038.0, 690.0, 1038.0, 723.0, 1053.25, 723.0 ],
					"source" : [ "obj-189", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 1053.250000000000227, 729.0, 1038.0, 729.0, 1038.0, 645.0, 1536.0, 645.0, 1536.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-189", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"midpoints" : [ 84.5, 1041.0, 84.5, 1041.0 ],
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-192", 0 ],
					"midpoints" : [ 911.250000000000114, 729.0, 911.250000000000114, 729.0 ],
					"order" : 1,
					"source" : [ "obj-193", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-288", 0 ],
					"midpoints" : [ 1000.750000000000114, 729.0, 1020.0, 729.0, 1020.0, 666.0, 969.5, 666.0 ],
					"source" : [ "obj-193", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-289", 0 ],
					"midpoints" : [ 956.000000000000114, 690.0, 888.0, 690.0, 888.0, 723.0, 910.900000000000091, 723.0 ],
					"source" : [ "obj-193", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 911.250000000000114, 729.0, 888.0, 729.0, 888.0, 645.0, 1536.0, 645.0, 1536.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-193", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-196", 0 ],
					"midpoints" : [ 764.250000000000114, 729.0, 764.250000000000114, 729.0 ],
					"order" : 1,
					"source" : [ "obj-197", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-285", 0 ],
					"midpoints" : [ 853.750000000000114, 729.0, 876.0, 729.0, 876.0, 666.0, 822.850000000000136, 666.0 ],
					"source" : [ "obj-197", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-286", 0 ],
					"midpoints" : [ 809.000000000000114, 690.0, 741.0, 690.0, 741.0, 723.0, 764.250000000000227, 723.0 ],
					"source" : [ "obj-197", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 764.250000000000114, 729.0, 741.0, 729.0, 741.0, 645.0, 1536.0, 645.0, 1536.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-197", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"midpoints" : [ 84.5, 1113.0, 84.5, 1113.0 ],
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"midpoints" : [ 125.5, 105.0, 125.5, 105.0 ],
					"source" : [ "obj-20", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-200", 0 ],
					"midpoints" : [ 619.250000000000114, 729.0, 619.250000000000114, 729.0 ],
					"order" : 1,
					"source" : [ "obj-201", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-282", 0 ],
					"midpoints" : [ 708.750000000000114, 729.0, 729.0, 729.0, 729.0, 666.0, 677.850000000000023, 666.0 ],
					"source" : [ "obj-201", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-283", 0 ],
					"midpoints" : [ 664.000000000000114, 690.0, 606.0, 690.0, 606.0, 723.0, 619.250000000000114, 723.0 ],
					"source" : [ "obj-201", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 619.250000000000114, 729.0, 594.0, 729.0, 594.0, 645.0, 1536.0, 645.0, 1536.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-201", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 1 ],
					"midpoints" : [ 142.44736842105263, 132.0, 102.0, 132.0, 102.0, 6.0, 773.937523961067086, 6.0 ],
					"source" : [ "obj-21", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 1 ],
					"midpoints" : [ 159.39473684210526, 132.0, 102.0, 132.0, 102.0, 6.0, 920.937523961067086, 6.0 ],
					"source" : [ "obj-21", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 1 ],
					"midpoints" : [ 176.34210526315789, 132.0, 102.0, 132.0, 102.0, 6.0, 1062.9375239610672, 6.0 ],
					"source" : [ "obj-21", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 1 ],
					"midpoints" : [ 244.131578947368439, 138.0, 273.0, 138.0, 273.0, 162.0, 585.0, 162.0, 585.0, 249.0, 1064.4375, 249.0 ],
					"source" : [ "obj-21", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 1 ],
					"midpoints" : [ 227.18421052631578, 138.0, 273.0, 138.0, 273.0, 162.0, 585.0, 162.0, 585.0, 249.0, 922.437500000000114, 249.0 ],
					"source" : [ "obj-21", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 1 ],
					"midpoints" : [ 210.236842105263179, 138.0, 273.0, 138.0, 273.0, 162.0, 585.0, 162.0, 585.0, 249.0, 775.437500000000114, 249.0 ],
					"source" : [ "obj-21", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 1 ],
					"midpoints" : [ 193.28947368421052, 138.0, 273.0, 138.0, 273.0, 162.0, 585.0, 162.0, 585.0, 276.0, 630.437500000000114, 276.0 ],
					"source" : [ "obj-21", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 1 ],
					"midpoints" : [ 311.921052631578959, 162.0, 585.0, 162.0, 585.0, 453.0, 1064.437500000000227, 453.0 ],
					"source" : [ "obj-21", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 1 ],
					"midpoints" : [ 294.973684210526358, 162.0, 585.0, 162.0, 585.0, 456.0, 922.437500000000114, 456.0 ],
					"source" : [ "obj-21", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 1 ],
					"midpoints" : [ 278.026315789473642, 162.0, 585.0, 162.0, 585.0, 456.0, 775.437500000000114, 456.0 ],
					"source" : [ "obj-21", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 1 ],
					"midpoints" : [ 261.078947368421041, 141.0, 585.0, 141.0, 585.0, 480.0, 630.437500000000114, 480.0 ],
					"source" : [ "obj-21", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 1 ],
					"midpoints" : [ 379.71052631578948, 162.0, 585.0, 162.0, 585.0, 666.0, 1064.437500000000227, 666.0 ],
					"source" : [ "obj-21", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 1 ],
					"midpoints" : [ 362.763157894736878, 162.0, 585.0, 162.0, 585.0, 666.0, 922.437500000000114, 666.0 ],
					"source" : [ "obj-21", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 1 ],
					"midpoints" : [ 345.81578947368422, 162.0, 585.0, 162.0, 585.0, 666.0, 775.437500000000114, 666.0 ],
					"source" : [ "obj-21", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 1 ],
					"midpoints" : [ 328.868421052631561, 162.0, 585.0, 162.0, 585.0, 690.0, 630.437500000000114, 690.0 ],
					"source" : [ "obj-21", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 1 ],
					"midpoints" : [ 447.5, 162.0, 585.0, 162.0, 585.0, 876.0, 1064.4375, 876.0 ],
					"source" : [ "obj-21", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 1 ],
					"midpoints" : [ 430.552631578947341, 162.0, 585.0, 162.0, 585.0, 876.0, 922.437500000000114, 876.0 ],
					"source" : [ "obj-21", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 1 ],
					"midpoints" : [ 413.60526315789474, 162.0, 585.0, 162.0, 585.0, 876.0, 775.437500000000114, 876.0 ],
					"source" : [ "obj-21", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 1 ],
					"midpoints" : [ 396.657894736842081, 162.0, 585.0, 162.0, 585.0, 900.0, 630.437500000000114, 900.0 ],
					"source" : [ "obj-21", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 1 ],
					"midpoints" : [ 125.5, 132.0, 102.0, 132.0, 102.0, 6.0, 628.937523961067086, 6.0 ],
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"midpoints" : [ 125.300000000000011, 231.0, 125.300000000000011, 231.0 ],
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-228", 0 ],
					"midpoints" : [ 1053.25, 939.0, 1053.25, 939.0 ],
					"order" : 1,
					"source" : [ "obj-229", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-279", 0 ],
					"midpoints" : [ 1142.75, 939.0, 1173.0, 939.0, 1173.0, 876.0, 1111.849999999999909, 876.0 ],
					"source" : [ "obj-229", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-280", 0 ],
					"midpoints" : [ 1098.0, 900.0, 1038.0, 900.0, 1038.0, 933.0, 1053.25, 933.0 ],
					"source" : [ "obj-229", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 1053.25, 939.0, 1038.0, 939.0, 1038.0, 858.0, 1452.0, 858.0, 1452.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-229", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 3 ],
					"midpoints" : [ 140.826315789473711, 273.0, 585.0, 273.0, 585.0, 225.0, 738.0, 225.0, 738.0, 60.0, 796.312523961067086, 60.0 ],
					"source" : [ "obj-23", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 3 ],
					"midpoints" : [ 156.352631578947381, 273.0, 585.0, 273.0, 585.0, 225.0, 885.0, 225.0, 885.0, 60.0, 943.312523961067086, 60.0 ],
					"source" : [ "obj-23", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 3 ],
					"midpoints" : [ 171.878947368421052, 273.0, 585.0, 273.0, 585.0, 33.0, 1085.3125239610672, 33.0 ],
					"source" : [ "obj-23", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 3 ],
					"midpoints" : [ 233.984210526315792, 273.0, 585.0, 273.0, 585.0, 249.0, 1086.8125, 249.0 ],
					"source" : [ "obj-23", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 3 ],
					"midpoints" : [ 218.457894736842121, 273.0, 585.0, 273.0, 585.0, 249.0, 944.812500000000114, 249.0 ],
					"source" : [ "obj-23", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 3 ],
					"midpoints" : [ 202.93157894736845, 273.0, 585.0, 273.0, 585.0, 249.0, 797.812500000000114, 249.0 ],
					"source" : [ "obj-23", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 3 ],
					"midpoints" : [ 187.405263157894751, 276.0, 652.812500000000114, 276.0 ],
					"source" : [ "obj-23", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 3 ],
					"midpoints" : [ 296.089473684210532, 306.0, 585.0, 306.0, 585.0, 453.0, 1086.812500000000227, 453.0 ],
					"source" : [ "obj-23", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 3 ],
					"midpoints" : [ 280.563157894736833, 306.0, 585.0, 306.0, 585.0, 456.0, 944.812500000000114, 456.0 ],
					"source" : [ "obj-23", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 3 ],
					"midpoints" : [ 265.03684210526319, 306.0, 585.0, 306.0, 585.0, 456.0, 797.812500000000114, 456.0 ],
					"source" : [ "obj-23", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 3 ],
					"midpoints" : [ 249.510526315789491, 306.0, 585.0, 306.0, 585.0, 480.0, 652.812500000000114, 480.0 ],
					"source" : [ "obj-23", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 3 ],
					"midpoints" : [ 358.194736842105272, 306.0, 585.0, 306.0, 585.0, 666.0, 1086.812500000000227, 666.0 ],
					"source" : [ "obj-23", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 3 ],
					"midpoints" : [ 342.668421052631629, 306.0, 585.0, 306.0, 585.0, 666.0, 944.812500000000114, 666.0 ],
					"source" : [ "obj-23", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 3 ],
					"midpoints" : [ 327.142105263157873, 306.0, 585.0, 306.0, 585.0, 666.0, 797.812500000000114, 666.0 ],
					"source" : [ "obj-23", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 3 ],
					"midpoints" : [ 311.615789473684231, 306.0, 585.0, 306.0, 585.0, 690.0, 652.812500000000114, 690.0 ],
					"source" : [ "obj-23", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 3 ],
					"midpoints" : [ 420.300000000000011, 306.0, 585.0, 306.0, 585.0, 876.0, 1086.8125, 876.0 ],
					"source" : [ "obj-23", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 3 ],
					"midpoints" : [ 404.773684210526312, 306.0, 585.0, 306.0, 585.0, 876.0, 944.812500000000114, 876.0 ],
					"source" : [ "obj-23", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 3 ],
					"midpoints" : [ 389.24736842105267, 306.0, 585.0, 306.0, 585.0, 876.0, 797.812500000000114, 876.0 ],
					"source" : [ "obj-23", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 3 ],
					"midpoints" : [ 373.721052631578971, 306.0, 585.0, 306.0, 585.0, 900.0, 652.812500000000114, 900.0 ],
					"source" : [ "obj-23", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 3 ],
					"midpoints" : [ 125.300000000000011, 273.0, 585.0, 273.0, 585.0, 60.0, 651.312523961067086, 60.0 ],
					"source" : [ "obj-23", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-232", 0 ],
					"midpoints" : [ 911.250000000000114, 939.0, 911.250000000000114, 939.0 ],
					"order" : 1,
					"source" : [ "obj-233", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-276", 0 ],
					"midpoints" : [ 1000.750000000000114, 939.0, 1020.0, 939.0, 1020.0, 876.0, 969.5, 876.0 ],
					"source" : [ "obj-233", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-277", 0 ],
					"midpoints" : [ 956.000000000000114, 900.0, 888.0, 900.0, 888.0, 933.0, 910.899999999999977, 933.0 ],
					"source" : [ "obj-233", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 911.250000000000114, 939.0, 888.0, 939.0, 888.0, 858.0, 1452.0, 858.0, 1452.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-233", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-236", 0 ],
					"midpoints" : [ 764.250000000000114, 939.0, 764.250000000000114, 939.0 ],
					"order" : 1,
					"source" : [ "obj-237", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-273", 0 ],
					"midpoints" : [ 853.750000000000114, 939.0, 876.0, 939.0, 876.0, 876.0, 822.850000000000136, 876.0 ],
					"source" : [ "obj-237", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-274", 0 ],
					"midpoints" : [ 809.000000000000114, 900.0, 741.0, 900.0, 741.0, 933.0, 764.250000000000114, 933.0 ],
					"source" : [ "obj-237", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 764.250000000000114, 939.0, 741.0, 939.0, 741.0, 858.0, 1452.0, 858.0, 1452.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-237", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-240", 0 ],
					"midpoints" : [ 619.250000000000114, 939.0, 619.250000000000114, 939.0 ],
					"order" : 1,
					"source" : [ "obj-241", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-267", 0 ],
					"midpoints" : [ 664.000000000000114, 900.0, 606.0, 900.0, 606.0, 933.0, 619.250000000000114, 933.0 ],
					"source" : [ "obj-241", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-269", 0 ],
					"midpoints" : [ 708.750000000000114, 939.0, 729.0, 939.0, 729.0, 876.0, 677.850000000000136, 876.0 ],
					"source" : [ "obj-241", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 619.250000000000114, 939.0, 594.0, 939.0, 594.0, 858.0, 1452.0, 858.0, 1452.0, 534.0, 1560.5, 534.0 ],
					"order" : 0,
					"source" : [ "obj-241", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 5 ],
					"midpoints" : [ 1239.5, 384.0, 1173.0, 384.0, 1173.0, 249.0, 1109.1875, 249.0 ],
					"order" : 0,
					"source" : [ "obj-245", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 5 ],
					"midpoints" : [ 1239.5, 384.0, 1173.0, 384.0, 1173.0, 249.0, 967.187500000000114, 249.0 ],
					"order" : 1,
					"source" : [ "obj-245", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 5 ],
					"midpoints" : [ 1239.5, 384.0, 1173.0, 384.0, 1173.0, 249.0, 820.187500000000114, 249.0 ],
					"order" : 2,
					"source" : [ "obj-245", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 5 ],
					"midpoints" : [ 1239.5, 384.0, 1173.0, 384.0, 1173.0, 249.0, 675.187500000000114, 249.0 ],
					"order" : 3,
					"source" : [ "obj-245", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 5 ],
					"midpoints" : [ 1239.5, 588.0, 1164.0, 588.0, 1164.0, 504.0, 1152.0, 504.0, 1152.0, 492.0, 1109.187500000000227, 492.0 ],
					"order" : 0,
					"source" : [ "obj-247", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 5 ],
					"midpoints" : [ 1239.5, 588.0, 1173.0, 588.0, 1173.0, 453.0, 967.187500000000114, 453.0 ],
					"order" : 1,
					"source" : [ "obj-247", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 5 ],
					"midpoints" : [ 1239.5, 588.0, 1173.0, 588.0, 1173.0, 453.0, 820.187500000000114, 453.0 ],
					"order" : 2,
					"source" : [ "obj-247", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 5 ],
					"midpoints" : [ 1239.5, 588.0, 1173.0, 588.0, 1173.0, 453.0, 675.187500000000114, 453.0 ],
					"order" : 3,
					"source" : [ "obj-247", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 5 ],
					"midpoints" : [ 1239.5, 807.0, 1173.0, 807.0, 1173.0, 666.0, 1109.187500000000227, 666.0 ],
					"order" : 0,
					"source" : [ "obj-249", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 5 ],
					"midpoints" : [ 1239.5, 807.0, 1173.0, 807.0, 1173.0, 666.0, 967.187500000000114, 666.0 ],
					"order" : 1,
					"source" : [ "obj-249", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 5 ],
					"midpoints" : [ 1239.5, 807.0, 1173.0, 807.0, 1173.0, 666.0, 820.187500000000114, 666.0 ],
					"order" : 2,
					"source" : [ "obj-249", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 5 ],
					"midpoints" : [ 1239.5, 807.0, 1173.0, 807.0, 1173.0, 666.0, 675.187500000000114, 666.0 ],
					"order" : 3,
					"source" : [ "obj-249", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"midpoints" : [ 123.300000000000011, 312.0, 123.300000000000011, 312.0 ],
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 5 ],
					"midpoints" : [ 1239.5, 1011.0, 1173.0, 1011.0, 1173.0, 876.0, 1109.1875, 876.0 ],
					"order" : 0,
					"source" : [ "obj-251", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 5 ],
					"midpoints" : [ 1239.5, 1011.0, 1173.0, 1011.0, 1173.0, 876.0, 967.187500000000114, 876.0 ],
					"order" : 1,
					"source" : [ "obj-251", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 5 ],
					"midpoints" : [ 1239.5, 1011.0, 1173.0, 1011.0, 1173.0, 876.0, 820.187500000000114, 876.0 ],
					"order" : 2,
					"source" : [ "obj-251", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 5 ],
					"midpoints" : [ 1239.5, 1011.0, 1173.0, 1011.0, 1173.0, 876.0, 675.187500000000114, 876.0 ],
					"order" : 3,
					"source" : [ "obj-251", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-245", 0 ],
					"midpoints" : [ 1389.5, 345.0, 1239.5, 345.0 ],
					"order" : 3,
					"source" : [ "obj-253", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-247", 0 ],
					"midpoints" : [ 1389.5, 549.0, 1239.5, 549.0 ],
					"order" : 2,
					"source" : [ "obj-253", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.615686274509804, 0.552941176470588, 0.827450980392157, 1.0 ],
					"destination" : [ "obj-249", 0 ],
					"midpoints" : [ 1389.5, 765.0, 1239.5, 765.0 ],
					"order" : 1,
					"source" : [ "obj-253", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-251", 0 ],
					"midpoints" : [ 1389.5, 969.0, 1239.5, 969.0 ],
					"order" : 0,
					"source" : [ "obj-253", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-68", 0 ],
					"midpoints" : [ 1389.5, 168.0, 1266.0, 168.0, 1266.0, 129.0, 1239.5, 129.0 ],
					"order" : 4,
					"source" : [ "obj-253", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 7 ],
					"midpoints" : [ 140.247368421052641, 345.0, 99.0, 345.0, 99.0, 273.0, 585.0, 273.0, 585.0, 225.0, 738.0, 225.0, 738.0, 60.0, 841.062523961067086, 60.0 ],
					"source" : [ "obj-26", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 7 ],
					"midpoints" : [ 157.194736842105272, 345.0, 99.0, 345.0, 99.0, 273.0, 585.0, 273.0, 585.0, 225.0, 885.0, 225.0, 885.0, 60.0, 988.062523961067086, 60.0 ],
					"source" : [ "obj-26", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 7 ],
					"midpoints" : [ 174.142105263157902, 345.0, 99.0, 345.0, 99.0, 273.0, 585.0, 273.0, 585.0, 33.0, 1122.0, 33.0, 1122.0, 66.0, 1130.0625239610672, 66.0 ],
					"source" : [ "obj-26", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 7 ],
					"midpoints" : [ 241.931578947368394, 345.0, 585.0, 345.0, 585.0, 249.0, 1125.0, 249.0, 1125.0, 282.0, 1131.5625, 282.0 ],
					"source" : [ "obj-26", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 7 ],
					"midpoints" : [ 224.984210526315792, 345.0, 585.0, 345.0, 585.0, 249.0, 981.0, 249.0, 981.0, 282.0, 989.562500000000114, 282.0 ],
					"source" : [ "obj-26", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 7 ],
					"midpoints" : [ 208.036842105263162, 345.0, 585.0, 345.0, 585.0, 249.0, 834.0, 249.0, 834.0, 282.0, 842.562500000000114, 282.0 ],
					"source" : [ "obj-26", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 7 ],
					"midpoints" : [ 191.089473684210532, 345.0, 99.0, 345.0, 99.0, 276.0, 697.562500000000114, 276.0 ],
					"source" : [ "obj-26", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 7 ],
					"midpoints" : [ 309.721052631578914, 375.0, 585.0, 375.0, 585.0, 453.0, 1125.0, 453.0, 1125.0, 486.0, 1131.562500000000227, 486.0 ],
					"source" : [ "obj-26", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 7 ],
					"midpoints" : [ 292.773684210526312, 375.0, 585.0, 375.0, 585.0, 456.0, 981.0, 456.0, 981.0, 486.0, 989.562500000000114, 486.0 ],
					"source" : [ "obj-26", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 7 ],
					"midpoints" : [ 275.826315789473711, 375.0, 585.0, 375.0, 585.0, 456.0, 834.0, 456.0, 834.0, 486.0, 842.562500000000114, 486.0 ],
					"source" : [ "obj-26", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 7 ],
					"midpoints" : [ 258.878947368421052, 375.0, 585.0, 375.0, 585.0, 480.0, 697.562500000000114, 480.0 ],
					"source" : [ "obj-26", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 7 ],
					"midpoints" : [ 377.510526315789434, 375.0, 585.0, 375.0, 585.0, 666.0, 1125.0, 666.0, 1125.0, 696.0, 1131.562500000000227, 696.0 ],
					"source" : [ "obj-26", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 7 ],
					"midpoints" : [ 360.563157894736833, 375.0, 585.0, 375.0, 585.0, 666.0, 981.0, 666.0, 981.0, 696.0, 989.562500000000114, 696.0 ],
					"source" : [ "obj-26", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 7 ],
					"midpoints" : [ 343.615789473684174, 375.0, 585.0, 375.0, 585.0, 666.0, 837.0, 666.0, 837.0, 699.0, 842.562500000000114, 699.0 ],
					"source" : [ "obj-26", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 7 ],
					"midpoints" : [ 326.668421052631516, 375.0, 585.0, 375.0, 585.0, 690.0, 697.562500000000114, 690.0 ],
					"source" : [ "obj-26", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 7 ],
					"midpoints" : [ 445.299999999999955, 375.0, 585.0, 375.0, 585.0, 876.0, 1125.0, 876.0, 1125.0, 906.0, 1131.5625, 906.0 ],
					"source" : [ "obj-26", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 7 ],
					"midpoints" : [ 428.352631578947353, 375.0, 585.0, 375.0, 585.0, 876.0, 981.0, 876.0, 981.0, 906.0, 989.562500000000114, 906.0 ],
					"source" : [ "obj-26", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 7 ],
					"midpoints" : [ 411.405263157894694, 375.0, 585.0, 375.0, 585.0, 876.0, 837.0, 876.0, 837.0, 909.0, 842.562500000000114, 909.0 ],
					"source" : [ "obj-26", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 7 ],
					"midpoints" : [ 394.457894736842093, 375.0, 585.0, 375.0, 585.0, 900.0, 697.562500000000114, 900.0 ],
					"source" : [ "obj-26", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 7 ],
					"midpoints" : [ 123.300000000000011, 345.0, 99.0, 345.0, 99.0, 273.0, 585.0, 273.0, 585.0, 60.0, 696.062523961067086, 60.0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"midpoints" : [ 123.300000000000011, 381.0, 123.300000000000011, 381.0 ],
					"source" : [ "obj-27", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 5 ],
					"midpoints" : [ 714.5, 915.0, 729.0, 915.0, 729.0, 876.0, 675.187500000000114, 876.0 ],
					"source" : [ "obj-271", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 5 ],
					"midpoints" : [ 859.5, 915.0, 876.0, 915.0, 876.0, 876.0, 820.187500000000114, 876.0 ],
					"source" : [ "obj-272", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 5 ],
					"midpoints" : [ 1006.149999999999864, 915.0, 1020.0, 915.0, 1020.0, 876.0, 967.187500000000114, 876.0 ],
					"source" : [ "obj-275", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 5 ],
					"midpoints" : [ 1148.499999999999773, 915.0, 1173.0, 915.0, 1173.0, 876.0, 1109.1875, 876.0 ],
					"source" : [ "obj-278", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 8 ],
					"midpoints" : [ 140.247368421052641, 422.5, 496.248696191059878, 422.5, 496.248696191059878, 62.16227263212204, 852.250023961067086, 62.16227263212204 ],
					"source" : [ "obj-28", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 8 ],
					"midpoints" : [ 157.194736842105272, 423.0, 585.0, 423.0, 585.0, 225.0, 885.0, 225.0, 885.0, 60.0, 993.0, 60.0, 993.0, 69.0, 999.250023961067086, 69.0 ],
					"source" : [ "obj-28", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 8 ],
					"midpoints" : [ 174.142105263157902, 423.0, 585.0, 423.0, 585.0, 33.0, 1122.0, 33.0, 1122.0, 69.0, 1141.2500239610672, 69.0 ],
					"source" : [ "obj-28", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 8 ],
					"midpoints" : [ 241.931578947368394, 423.0, 585.0, 423.0, 585.0, 249.0, 1125.0, 249.0, 1125.0, 285.0, 1142.75, 285.0 ],
					"source" : [ "obj-28", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 8 ],
					"midpoints" : [ 224.984210526315792, 423.0, 585.0, 423.0, 585.0, 249.0, 981.0, 249.0, 981.0, 285.0, 1000.750000000000114, 285.0 ],
					"source" : [ "obj-28", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 8 ],
					"midpoints" : [ 208.036842105263162, 423.0, 585.0, 423.0, 585.0, 249.0, 834.0, 249.0, 834.0, 285.0, 853.750000000000114, 285.0 ],
					"source" : [ "obj-28", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 8 ],
					"midpoints" : [ 191.089473684210532, 423.0, 585.0, 423.0, 585.0, 276.0, 699.0, 276.0, 699.0, 285.0, 708.750000000000114, 285.0 ],
					"source" : [ "obj-28", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 8 ],
					"midpoints" : [ 309.721052631578914, 453.0, 1125.0, 453.0, 1125.0, 492.0, 1142.750000000000227, 492.0 ],
					"source" : [ "obj-28", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 8 ],
					"midpoints" : [ 292.773684210526312, 456.0, 981.0, 456.0, 981.0, 492.0, 1000.750000000000114, 492.0 ],
					"source" : [ "obj-28", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 8 ],
					"midpoints" : [ 275.826315789473711, 456.0, 834.0, 456.0, 834.0, 489.0, 853.750000000000114, 489.0 ],
					"source" : [ "obj-28", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 8 ],
					"midpoints" : [ 258.878947368421052, 480.0, 699.0, 480.0, 699.0, 489.0, 708.750000000000114, 489.0 ],
					"source" : [ "obj-28", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 8 ],
					"midpoints" : [ 377.510526315789434, 666.0, 1125.0, 666.0, 1125.0, 699.0, 1142.750000000000227, 699.0 ],
					"source" : [ "obj-28", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 8 ],
					"midpoints" : [ 360.563157894736833, 666.0, 981.0, 666.0, 981.0, 699.0, 1000.750000000000114, 699.0 ],
					"source" : [ "obj-28", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 8 ],
					"midpoints" : [ 343.615789473684174, 666.0, 837.0, 666.0, 837.0, 699.0, 853.750000000000114, 699.0 ],
					"source" : [ "obj-28", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 8 ],
					"midpoints" : [ 326.668421052631516, 690.0, 699.0, 690.0, 699.0, 699.0, 708.750000000000114, 699.0 ],
					"source" : [ "obj-28", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 8 ],
					"midpoints" : [ 445.299999999999955, 876.0, 1125.0, 876.0, 1125.0, 909.0, 1142.75, 909.0 ],
					"source" : [ "obj-28", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 8 ],
					"midpoints" : [ 428.352631578947353, 876.0, 981.0, 876.0, 981.0, 909.0, 1000.750000000000114, 909.0 ],
					"source" : [ "obj-28", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 8 ],
					"midpoints" : [ 411.405263157894694, 876.0, 837.0, 876.0, 837.0, 909.0, 853.750000000000114, 909.0 ],
					"source" : [ "obj-28", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 8 ],
					"midpoints" : [ 394.457894736842093, 900.0, 702.0, 900.0, 702.0, 909.0, 708.750000000000114, 909.0 ],
					"source" : [ "obj-28", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 8 ],
					"midpoints" : [ 123.300000000000011, 423.0, 585.0, 423.0, 585.0, 60.0, 699.0, 60.0, 699.0, 69.0, 707.250023961067086, 69.0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 5 ],
					"midpoints" : [ 714.499999999999886, 705.0, 729.0, 705.0, 729.0, 666.0, 675.187500000000114, 666.0 ],
					"source" : [ "obj-281", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 5 ],
					"midpoints" : [ 859.5, 705.0, 876.0, 705.0, 876.0, 666.0, 820.187500000000114, 666.0 ],
					"source" : [ "obj-284", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 5 ],
					"midpoints" : [ 1006.149999999999864, 705.0, 1020.0, 705.0, 1020.0, 666.0, 967.187500000000114, 666.0 ],
					"source" : [ "obj-287", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 5 ],
					"midpoints" : [ 1148.499999999999773, 705.0, 1173.0, 705.0, 1173.0, 666.0, 1109.187500000000227, 666.0 ],
					"source" : [ "obj-290", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 5 ],
					"midpoints" : [ 1148.499999999999773, 492.0, 1109.187500000000227, 492.0 ],
					"source" : [ "obj-293", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 5 ],
					"midpoints" : [ 1006.149999999999864, 492.0, 967.187500000000114, 492.0 ],
					"source" : [ "obj-296", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 5 ],
					"midpoints" : [ 859.499999999999886, 495.0, 873.0, 495.0, 873.0, 456.0, 820.187500000000114, 456.0 ],
					"source" : [ "obj-299", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 5 ],
					"midpoints" : [ 714.499999999999886, 495.0, 729.0, 495.0, 729.0, 456.0, 675.187500000000114, 456.0 ],
					"source" : [ "obj-302", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 5 ],
					"midpoints" : [ 713.000023961066859, 288.0, 729.0, 288.0, 729.0, 249.0, 675.187500000000114, 249.0 ],
					"source" : [ "obj-305", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 5 ],
					"midpoints" : [ 858.000023961067086, 288.0, 873.0, 288.0, 873.0, 249.0, 820.187500000000114, 249.0 ],
					"source" : [ "obj-308", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 5 ],
					"midpoints" : [ 1006.149999999999864, 288.0, 1020.0, 288.0, 1020.0, 249.0, 967.187500000000114, 249.0 ],
					"source" : [ "obj-311", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 5 ],
					"midpoints" : [ 1148.499999999999773, 288.0, 1173.0, 288.0, 1173.0, 249.0, 1109.1875, 249.0 ],
					"source" : [ "obj-314", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 5 ],
					"midpoints" : [ 1006.149999999999864, 72.0, 1020.0, 72.0, 1020.0, 33.0, 965.687523961067086, 33.0 ],
					"source" : [ "obj-317", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 5 ],
					"midpoints" : [ 1147.000023961066972, 72.0, 1173.0, 72.0, 1173.0, 33.0, 1107.6875239610672, 33.0 ],
					"source" : [ "obj-320", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 5 ],
					"midpoints" : [ 858.000023961066859, 72.0, 873.0, 72.0, 873.0, 33.0, 818.687523961067086, 33.0 ],
					"source" : [ "obj-323", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 5 ],
					"midpoints" : [ 713.000023961066859, 72.0, 729.0, 72.0, 729.0, 33.0, 673.687523961067086, 33.0 ],
					"source" : [ "obj-326", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"midpoints" : [ 125.5, 45.0, 125.5, 45.0 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 0 ],
					"midpoints" : [ 142.44736842105263, 75.0, 102.0, 75.0, 102.0, 6.0, 762.750023961067086, 6.0 ],
					"source" : [ "obj-38", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 0 ],
					"midpoints" : [ 159.39473684210526, 75.0, 102.0, 75.0, 102.0, 6.0, 909.750023961067086, 6.0 ],
					"source" : [ "obj-38", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 0 ],
					"midpoints" : [ 176.34210526315789, 75.0, 102.0, 75.0, 102.0, 6.0, 1051.7500239610672, 6.0 ],
					"source" : [ "obj-38", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 0 ],
					"midpoints" : [ 244.131578947368439, 75.0, 270.0, 75.0, 270.0, 96.0, 585.0, 96.0, 585.0, 249.0, 1053.25, 249.0 ],
					"source" : [ "obj-38", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 0 ],
					"midpoints" : [ 227.18421052631578, 75.0, 270.0, 75.0, 270.0, 96.0, 585.0, 96.0, 585.0, 249.0, 911.250000000000114, 249.0 ],
					"source" : [ "obj-38", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-157", 0 ],
					"midpoints" : [ 210.236842105263179, 75.0, 270.0, 75.0, 270.0, 96.0, 585.0, 96.0, 585.0, 249.0, 764.250000000000114, 249.0 ],
					"source" : [ "obj-38", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-161", 0 ],
					"midpoints" : [ 193.28947368421052, 75.0, 270.0, 75.0, 270.0, 96.0, 585.0, 96.0, 585.0, 276.0, 619.250000000000114, 276.0 ],
					"source" : [ "obj-38", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-169", 0 ],
					"midpoints" : [ 311.921052631578959, 96.0, 585.0, 96.0, 585.0, 453.0, 1053.250000000000227, 453.0 ],
					"source" : [ "obj-38", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-173", 0 ],
					"midpoints" : [ 294.973684210526358, 96.0, 585.0, 96.0, 585.0, 456.0, 911.250000000000114, 456.0 ],
					"source" : [ "obj-38", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-177", 0 ],
					"midpoints" : [ 278.026315789473642, 96.0, 585.0, 96.0, 585.0, 456.0, 764.250000000000114, 456.0 ],
					"source" : [ "obj-38", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-181", 0 ],
					"midpoints" : [ 261.078947368421041, 84.0, 585.0, 84.0, 585.0, 480.0, 619.250000000000114, 480.0 ],
					"source" : [ "obj-38", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-189", 0 ],
					"midpoints" : [ 379.71052631578948, 96.0, 585.0, 96.0, 585.0, 666.0, 1053.250000000000227, 666.0 ],
					"source" : [ "obj-38", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-193", 0 ],
					"midpoints" : [ 362.763157894736878, 96.0, 585.0, 96.0, 585.0, 666.0, 911.250000000000114, 666.0 ],
					"source" : [ "obj-38", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-197", 0 ],
					"midpoints" : [ 345.81578947368422, 96.0, 585.0, 96.0, 585.0, 666.0, 764.250000000000114, 666.0 ],
					"source" : [ "obj-38", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-201", 0 ],
					"midpoints" : [ 328.868421052631561, 96.0, 585.0, 96.0, 585.0, 690.0, 619.250000000000114, 690.0 ],
					"source" : [ "obj-38", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-229", 0 ],
					"midpoints" : [ 447.5, 96.0, 585.0, 96.0, 585.0, 876.0, 1053.25, 876.0 ],
					"source" : [ "obj-38", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-233", 0 ],
					"midpoints" : [ 430.552631578947341, 96.0, 585.0, 96.0, 585.0, 876.0, 911.250000000000114, 876.0 ],
					"source" : [ "obj-38", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-237", 0 ],
					"midpoints" : [ 413.60526315789474, 96.0, 585.0, 96.0, 585.0, 876.0, 764.250000000000114, 876.0 ],
					"source" : [ "obj-38", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-241", 0 ],
					"midpoints" : [ 396.657894736842081, 96.0, 585.0, 96.0, 585.0, 900.0, 619.250000000000114, 900.0 ],
					"source" : [ "obj-38", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 0 ],
					"midpoints" : [ 125.5, 75.0, 102.0, 75.0, 102.0, 6.0, 617.750023961067086, 6.0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-253", 0 ],
					"midpoints" : [ 1389.5, 120.0, 1389.5, 120.0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-129", 5 ],
					"midpoints" : [ 1239.5, 162.0, 1173.0, 162.0, 1173.0, 33.0, 818.687523961067086, 33.0 ],
					"order" : 2,
					"source" : [ "obj-68", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 5 ],
					"midpoints" : [ 1239.5, 162.0, 1173.0, 162.0, 1173.0, 33.0, 965.687523961067086, 33.0 ],
					"order" : 1,
					"source" : [ "obj-68", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-137", 5 ],
					"midpoints" : [ 1239.5, 162.0, 1173.0, 162.0, 1173.0, 33.0, 1107.6875239610672, 33.0 ],
					"order" : 0,
					"source" : [ "obj-68", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 5 ],
					"midpoints" : [ 1239.5, 162.0, 1173.0, 162.0, 1173.0, 33.0, 673.687523961067086, 33.0 ],
					"order" : 3,
					"source" : [ "obj-68", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-327", 0 ],
					"midpoints" : [ 707.250023961067086, 96.0, 676.350023961066995, 96.0 ],
					"source" : [ "obj-77", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-328", 0 ],
					"midpoints" : [ 662.500023961067086, 60.0, 594.0, 60.0, 594.0, 93.0, 617.750023961067086, 93.0 ],
					"source" : [ "obj-77", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 617.750023961067086, 96.0, 585.0, 96.0, 585.0, 453.0, 1560.5, 453.0 ],
					"order" : 0,
					"source" : [ "obj-77", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-76", 0 ],
					"midpoints" : [ 617.750023961067086, 96.0, 617.750023961067086, 96.0 ],
					"order" : 1,
					"source" : [ "obj-77", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"midpoints" : [ 84.5, 1185.0, 84.5, 1185.0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"midpoints" : [ 1592.421988058090164, 45.0, 1592.421988058090164, 45.0 ],
					"source" : [ "obj-9", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-104", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 726.0, 84.5, 726.0 ],
					"order" : 7,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-105", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 798.0, 84.5, 798.0 ],
					"order" : 6,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-106", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 870.0, 84.5, 870.0 ],
					"order" : 5,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-107", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 942.0, 84.5, 942.0 ],
					"order" : 4,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-108", 0 ],
					"midpoints" : [ 84.5, 624.0, 231.0, 624.0, 231.0, 612.0, 255.5, 612.0 ],
					"order" : 0,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 1011.0, 84.5, 1011.0 ],
					"order" : 3,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 1083.0, 84.5, 1083.0 ],
					"order" : 2,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"midpoints" : [ 84.5, 648.0, 60.0, 648.0, 60.0, 1155.0, 84.5, 1155.0 ],
					"order" : 1,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-98", 0 ],
					"midpoints" : [ 84.5, 615.0, 84.5, 615.0 ],
					"order" : 8,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 0 ],
					"midpoints" : [ 84.5, 684.0, 84.5, 684.0 ],
					"source" : [ "obj-98", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"parameterbanks" : 			{

			}

		}
,
		"dependency_cache" : [ 			{
				"name" : "phalanx~.maxpat",
				"bootpath" : "~/Projects/u-mano/umano/onehand/max",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
 ],
		"autosave" : 0,
		"boxgroups" : [ 			{
				"boxes" : [ "obj-124", "obj-76", "obj-81" ]
			}
, 			{
				"boxes" : [ "obj-130", "obj-128", "obj-127" ]
			}
, 			{
				"boxes" : [ "obj-134", "obj-132", "obj-131" ]
			}
, 			{
				"boxes" : [ "obj-138", "obj-136", "obj-135" ]
			}
, 			{
				"boxes" : [ "obj-162", "obj-160", "obj-159" ]
			}
, 			{
				"boxes" : [ "obj-158", "obj-156", "obj-155" ]
			}
, 			{
				"boxes" : [ "obj-154", "obj-152", "obj-151" ]
			}
, 			{
				"boxes" : [ "obj-150", "obj-148", "obj-147" ]
			}
, 			{
				"boxes" : [ "obj-182", "obj-180", "obj-179" ]
			}
, 			{
				"boxes" : [ "obj-178", "obj-176", "obj-175" ]
			}
, 			{
				"boxes" : [ "obj-174", "obj-172", "obj-171" ]
			}
, 			{
				"boxes" : [ "obj-170", "obj-168", "obj-167" ]
			}
, 			{
				"boxes" : [ "obj-202", "obj-200", "obj-199" ]
			}
, 			{
				"boxes" : [ "obj-198", "obj-196", "obj-195" ]
			}
, 			{
				"boxes" : [ "obj-194", "obj-192", "obj-191" ]
			}
, 			{
				"boxes" : [ "obj-190", "obj-188", "obj-187" ]
			}
, 			{
				"boxes" : [ "obj-242", "obj-240", "obj-239" ]
			}
, 			{
				"boxes" : [ "obj-238", "obj-236", "obj-235" ]
			}
, 			{
				"boxes" : [ "obj-234", "obj-232", "obj-231" ]
			}
, 			{
				"boxes" : [ "obj-230", "obj-228", "obj-227" ]
			}
 ]
	}

}
