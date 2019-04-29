# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import glob
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

folname = sys.argv[1]

folder = '{}_vtks'.format(folname)
# Paraview 5.6 changes so we have to use a calculator for some
# stupid reason to extract the component colour for the Glyphs.
colour_by = 'Z'
assert colour_by in ['X', 'Y', 'Z']
colorbar = False

files = sorted(glob.glob(folder + '/m_*.vtk'))

m_000 = LegacyVTKReader(FileNames=files)
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1129, 646]
#
# # show data in view
# m_000Display = Show(m_000, renderView1)
#
# # trace defaults for the display properties.
# m_000Display.Representation = 'Outline'
# m_000Display.AmbientColor = [1.0, 1.0, 1.0]
# m_000Display.ColorArrayName = ['CELLS', '']
# m_000Display.DiffuseColor = [1.0, 1.0, 1.0]
# m_000Display.LookupTable = None
# m_000Display.MapScalars = 1
# m_000Display.MultiComponentsMapping = 0
# m_000Display.InterpolateScalarsBeforeMapping = 1
# m_000Display.Opacity = 1.0
# m_000Display.PointSize = 2.0
# m_000Display.LineWidth = 1.0
# m_000Display.RenderLinesAsTubes = 0
# m_000Display.RenderPointsAsSpheres = 0
# m_000Display.Interpolation = 'Gouraud'
# m_000Display.Specular = 0.0
# m_000Display.SpecularColor = [1.0, 1.0, 1.0]
# m_000Display.SpecularPower = 100.0
# m_000Display.Luminosity = 0.0
# m_000Display.Ambient = 0.0
# m_000Display.Diffuse = 1.0
# m_000Display.EdgeColor = [0.0, 0.0, 0.5]
# m_000Display.BackfaceRepresentation = 'Follow Frontface'
# m_000Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
# m_000Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
# m_000Display.BackfaceOpacity = 1.0
# m_000Display.Position = [0.0, 0.0, 0.0]
# m_000Display.Scale = [1.0, 1.0, 1.0]
# m_000Display.Orientation = [0.0, 0.0, 0.0]
# m_000Display.Origin = [0.0, 0.0, 0.0]
# m_000Display.Pickable = 1
# m_000Display.Texture = None
# m_000Display.Triangulate = 0
# m_000Display.UseShaderReplacements = 0
# m_000Display.ShaderReplacements = ''
# m_000Display.NonlinearSubdivisionLevel = 1
# m_000Display.UseDataPartitions = 0
# m_000Display.OSPRayUseScaleArray = 0
# m_000Display.OSPRayScaleArray = ''
# m_000Display.OSPRayScaleFunction = 'PiecewiseFunction'
# m_000Display.OSPRayMaterial = 'None'
# m_000Display.Orient = 0
# m_000Display.OrientationMode = 'Direction'
# m_000Display.SelectOrientationVectors = 'spins'
# m_000Display.Scaling = 0
# m_000Display.ScaleMode = 'No Data Scaling Off'
# m_000Display.ScaleFactor = 5.0
# m_000Display.SelectScaleArray = 'M_s'
# m_000Display.GlyphType = 'Arrow'
# m_000Display.UseGlyphTable = 0
# m_000Display.GlyphTableIndexArray = 'M_s'
# m_000Display.UseCompositeGlyphTable = 0
# m_000Display.UseGlyphCullingAndLOD = 0
# m_000Display.LODValues = []
# m_000Display.ColorByLODIndex = 0
# m_000Display.GaussianRadius = 0.25
# m_000Display.ShaderPreset = 'Sphere'
# m_000Display.CustomTriangleScale = 3
# m_000Display.CustomShader = """ // This custom shader code define a gaussian blur
#  // Please take a look into vtkSMPointGaussianRepresentation.cxx
#  // for other custom shader examples
#  //VTK::Color::Impl
#    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
#    float gaussian = exp(-0.5*dist2);
#    opacity = opacity*gaussian;
# """
# m_000Display.Emissive = 0
# m_000Display.ScaleByArray = 0
# m_000Display.SetScaleArray = [None, '']
# m_000Display.ScaleArrayComponent = 0
# m_000Display.UseScaleFunction = 1
# m_000Display.ScaleTransferFunction = 'PiecewiseFunction'
# m_000Display.OpacityByArray = 0
# m_000Display.OpacityArray = [None, '']
# m_000Display.OpacityArrayComponent = 0
# m_000Display.OpacityTransferFunction = 'PiecewiseFunction'
# m_000Display.DataAxesGrid = 'GridAxesRepresentation'
# m_000Display.SelectionCellLabelBold = 0
# m_000Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
# m_000Display.SelectionCellLabelFontFamily = 'Arial'
# m_000Display.SelectionCellLabelFontFile = ''
# m_000Display.SelectionCellLabelFontSize = 18
# m_000Display.SelectionCellLabelItalic = 0
# m_000Display.SelectionCellLabelJustification = 'Left'
# m_000Display.SelectionCellLabelOpacity = 1.0
# m_000Display.SelectionCellLabelShadow = 0
# m_000Display.SelectionPointLabelBold = 0
# m_000Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
# m_000Display.SelectionPointLabelFontFamily = 'Arial'
# m_000Display.SelectionPointLabelFontFile = ''
# m_000Display.SelectionPointLabelFontSize = 18
# m_000Display.SelectionPointLabelItalic = 0
# m_000Display.SelectionPointLabelJustification = 'Left'
# m_000Display.SelectionPointLabelOpacity = 1.0
# m_000Display.SelectionPointLabelShadow = 0
# m_000Display.PolarAxes = 'PolarAxesRepresentation'
#
# # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
# m_000Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# m_000Display.OSPRayScaleFunction.UseLogScale = 0
#
# # init the 'Arrow' selected for 'GlyphType'
# m_000Display.GlyphType.TipResolution = 6
# m_000Display.GlyphType.TipRadius = 0.1
# m_000Display.GlyphType.TipLength = 0.35
# m_000Display.GlyphType.ShaftResolution = 6
# m_000Display.GlyphType.ShaftRadius = 0.03
# m_000Display.GlyphType.Invert = 0
#
# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# m_000Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# m_000Display.ScaleTransferFunction.UseLogScale = 0
#
# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# m_000Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# m_000Display.OpacityTransferFunction.UseLogScale = 0
#
# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# m_000Display.DataAxesGrid.XTitle = 'X Axis'
# m_000Display.DataAxesGrid.YTitle = 'Y Axis'
# m_000Display.DataAxesGrid.ZTitle = 'Z Axis'
# m_000Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.XTitleFontFamily = 'Arial'
# m_000Display.DataAxesGrid.XTitleFontFile = ''
# m_000Display.DataAxesGrid.XTitleBold = 0
# m_000Display.DataAxesGrid.XTitleItalic = 0
# m_000Display.DataAxesGrid.XTitleFontSize = 12
# m_000Display.DataAxesGrid.XTitleShadow = 0
# m_000Display.DataAxesGrid.XTitleOpacity = 1.0
# m_000Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.YTitleFontFamily = 'Arial'
# m_000Display.DataAxesGrid.YTitleFontFile = ''
# m_000Display.DataAxesGrid.YTitleBold = 0
# m_000Display.DataAxesGrid.YTitleItalic = 0
# m_000Display.DataAxesGrid.YTitleFontSize = 12
# m_000Display.DataAxesGrid.YTitleShadow = 0
# m_000Display.DataAxesGrid.YTitleOpacity = 1.0
# m_000Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
# m_000Display.DataAxesGrid.ZTitleFontFile = ''
# m_000Display.DataAxesGrid.ZTitleBold = 0
# m_000Display.DataAxesGrid.ZTitleItalic = 0
# m_000Display.DataAxesGrid.ZTitleFontSize = 12
# m_000Display.DataAxesGrid.ZTitleShadow = 0
# m_000Display.DataAxesGrid.ZTitleOpacity = 1.0
# m_000Display.DataAxesGrid.FacesToRender = 63
# m_000Display.DataAxesGrid.CullBackface = 0
# m_000Display.DataAxesGrid.CullFrontface = 1
# m_000Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.ShowGrid = 0
# m_000Display.DataAxesGrid.ShowEdges = 1
# m_000Display.DataAxesGrid.ShowTicks = 1
# m_000Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
# m_000Display.DataAxesGrid.AxesToLabel = 63
# m_000Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.XLabelFontFamily = 'Arial'
# m_000Display.DataAxesGrid.XLabelFontFile = ''
# m_000Display.DataAxesGrid.XLabelBold = 0
# m_000Display.DataAxesGrid.XLabelItalic = 0
# m_000Display.DataAxesGrid.XLabelFontSize = 12
# m_000Display.DataAxesGrid.XLabelShadow = 0
# m_000Display.DataAxesGrid.XLabelOpacity = 1.0
# m_000Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.YLabelFontFamily = 'Arial'
# m_000Display.DataAxesGrid.YLabelFontFile = ''
# m_000Display.DataAxesGrid.YLabelBold = 0
# m_000Display.DataAxesGrid.YLabelItalic = 0
# m_000Display.DataAxesGrid.YLabelFontSize = 12
# m_000Display.DataAxesGrid.YLabelShadow = 0
# m_000Display.DataAxesGrid.YLabelOpacity = 1.0
# m_000Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
# m_000Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
# m_000Display.DataAxesGrid.ZLabelFontFile = ''
# m_000Display.DataAxesGrid.ZLabelBold = 0
# m_000Display.DataAxesGrid.ZLabelItalic = 0
# m_000Display.DataAxesGrid.ZLabelFontSize = 12
# m_000Display.DataAxesGrid.ZLabelShadow = 0
# m_000Display.DataAxesGrid.ZLabelOpacity = 1.0
# m_000Display.DataAxesGrid.XAxisNotation = 'Mixed'
# m_000Display.DataAxesGrid.XAxisPrecision = 2
# m_000Display.DataAxesGrid.XAxisUseCustomLabels = 0
# m_000Display.DataAxesGrid.XAxisLabels = []
# m_000Display.DataAxesGrid.YAxisNotation = 'Mixed'
# m_000Display.DataAxesGrid.YAxisPrecision = 2
# m_000Display.DataAxesGrid.YAxisUseCustomLabels = 0
# m_000Display.DataAxesGrid.YAxisLabels = []
# m_000Display.DataAxesGrid.ZAxisNotation = 'Mixed'
# m_000Display.DataAxesGrid.ZAxisPrecision = 2
# m_000Display.DataAxesGrid.ZAxisUseCustomLabels = 0
# m_000Display.DataAxesGrid.ZAxisLabels = []
#
# # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
# m_000Display.PolarAxes.Visibility = 0
# m_000Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
# m_000Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
# m_000Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
# m_000Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
# m_000Display.PolarAxes.EnableCustomRange = 0
# m_000Display.PolarAxes.CustomRange = [0.0, 1.0]
# m_000Display.PolarAxes.PolarAxisVisibility = 1
# m_000Display.PolarAxes.RadialAxesVisibility = 1
# m_000Display.PolarAxes.DrawRadialGridlines = 1
# m_000Display.PolarAxes.PolarArcsVisibility = 1
# m_000Display.PolarAxes.DrawPolarArcsGridlines = 1
# m_000Display.PolarAxes.NumberOfRadialAxes = 0
# m_000Display.PolarAxes.AutoSubdividePolarAxis = 1
# m_000Display.PolarAxes.NumberOfPolarAxis = 0
# m_000Display.PolarAxes.MinimumRadius = 0.0
# m_000Display.PolarAxes.MinimumAngle = 0.0
# m_000Display.PolarAxes.MaximumAngle = 90.0
# m_000Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
# m_000Display.PolarAxes.Ratio = 1.0
# m_000Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.PolarAxisTitleVisibility = 1
# m_000Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
# m_000Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
# m_000Display.PolarAxes.PolarLabelVisibility = 1
# m_000Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
# m_000Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
# m_000Display.PolarAxes.RadialLabelVisibility = 1
# m_000Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
# m_000Display.PolarAxes.RadialLabelLocation = 'Bottom'
# m_000Display.PolarAxes.RadialUnitsVisibility = 1
# m_000Display.PolarAxes.ScreenSize = 10.0
# m_000Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.PolarAxisTitleOpacity = 1.0
# m_000Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
# m_000Display.PolarAxes.PolarAxisTitleFontFile = ''
# m_000Display.PolarAxes.PolarAxisTitleBold = 0
# m_000Display.PolarAxes.PolarAxisTitleItalic = 0
# m_000Display.PolarAxes.PolarAxisTitleShadow = 0
# m_000Display.PolarAxes.PolarAxisTitleFontSize = 12
# m_000Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.PolarAxisLabelOpacity = 1.0
# m_000Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
# m_000Display.PolarAxes.PolarAxisLabelFontFile = ''
# m_000Display.PolarAxes.PolarAxisLabelBold = 0
# m_000Display.PolarAxes.PolarAxisLabelItalic = 0
# m_000Display.PolarAxes.PolarAxisLabelShadow = 0
# m_000Display.PolarAxes.PolarAxisLabelFontSize = 12
# m_000Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
# m_000Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
# m_000Display.PolarAxes.LastRadialAxisTextFontFile = ''
# m_000Display.PolarAxes.LastRadialAxisTextBold = 0
# m_000Display.PolarAxes.LastRadialAxisTextItalic = 0
# m_000Display.PolarAxes.LastRadialAxisTextShadow = 0
# m_000Display.PolarAxes.LastRadialAxisTextFontSize = 12
# m_000Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
# m_000Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
# m_000Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
# m_000Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
# m_000Display.PolarAxes.SecondaryRadialAxesTextBold = 0
# m_000Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
# m_000Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
# m_000Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
# m_000Display.PolarAxes.EnableDistanceLOD = 1
# m_000Display.PolarAxes.DistanceLODThreshold = 0.7
# m_000Display.PolarAxes.EnableViewAngleLOD = 1
# m_000Display.PolarAxes.ViewAngleLODThreshold = 0.7
# m_000Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
# m_000Display.PolarAxes.PolarTicksVisibility = 1
# m_000Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
# m_000Display.PolarAxes.TickLocation = 'Both'
# m_000Display.PolarAxes.AxisTickVisibility = 1
# m_000Display.PolarAxes.AxisMinorTickVisibility = 0
# m_000Display.PolarAxes.ArcTickVisibility = 1
# m_000Display.PolarAxes.ArcMinorTickVisibility = 0
# m_000Display.PolarAxes.DeltaAngleMajor = 10.0
# m_000Display.PolarAxes.DeltaAngleMinor = 5.0
# m_000Display.PolarAxes.PolarAxisMajorTickSize = 0.0
# m_000Display.PolarAxes.PolarAxisTickRatioSize = 0.3
# m_000Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
# m_000Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
# m_000Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
# m_000Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
# m_000Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
# m_000Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
# m_000Display.PolarAxes.ArcMajorTickSize = 0.0
# m_000Display.PolarAxes.ArcTickRatioSize = 0.3
# m_000Display.PolarAxes.ArcMajorTickThickness = 1.0
# m_000Display.PolarAxes.ArcTickRatioThickness = 0.5
# m_000Display.PolarAxes.Use2DMode = 0
# m_000Display.PolarAxes.UseLogAxis = 0

# # reset view to fit data
renderView1.ResetCamera()

# # get the material library
# materialLibrary1 = GetMaterialLibrary()
#
# # update the view to ensure updated data information
# renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=m_000)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'

# Properties modified on calculator1
calculator1.AttributeType = 'Cell Data'
calculator1.Function = 'spins_{}'.format(colour_by)

# # show data in view
# calculator1Display = Show(calculator1, renderView1)
#
# # trace defaults for the display properties.
# calculator1Display.Representation = 'Outline'
# calculator1Display.AmbientColor = [1.0, 1.0, 1.0]
# calculator1Display.ColorArrayName = ['CELLS', '']
# calculator1Display.DiffuseColor = [1.0, 1.0, 1.0]
# calculator1Display.LookupTable = None
# calculator1Display.MapScalars = 1
# calculator1Display.MultiComponentsMapping = 0
# calculator1Display.InterpolateScalarsBeforeMapping = 1
# calculator1Display.Opacity = 1.0
# calculator1Display.PointSize = 2.0
# calculator1Display.LineWidth = 1.0
# calculator1Display.RenderLinesAsTubes = 0
# calculator1Display.RenderPointsAsSpheres = 0
# calculator1Display.Interpolation = 'Gouraud'
# calculator1Display.Specular = 0.0
# calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
# calculator1Display.SpecularPower = 100.0
# calculator1Display.Luminosity = 0.0
# calculator1Display.Ambient = 0.0
# calculator1Display.Diffuse = 1.0
# calculator1Display.EdgeColor = [0.0, 0.0, 0.5]
# calculator1Display.BackfaceRepresentation = 'Follow Frontface'
# calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
# calculator1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
# calculator1Display.BackfaceOpacity = 1.0
# calculator1Display.Position = [0.0, 0.0, 0.0]
# calculator1Display.Scale = [1.0, 1.0, 1.0]
# calculator1Display.Orientation = [0.0, 0.0, 0.0]
# calculator1Display.Origin = [0.0, 0.0, 0.0]
# calculator1Display.Pickable = 1
# calculator1Display.Texture = None
# calculator1Display.Triangulate = 0
# calculator1Display.UseShaderReplacements = 0
# calculator1Display.ShaderReplacements = ''
# calculator1Display.NonlinearSubdivisionLevel = 1
# calculator1Display.UseDataPartitions = 0
# calculator1Display.OSPRayUseScaleArray = 0
# calculator1Display.OSPRayScaleArray = ''
# calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# calculator1Display.OSPRayMaterial = 'None'
# calculator1Display.Orient = 0
# calculator1Display.OrientationMode = 'Direction'
# calculator1Display.SelectOrientationVectors = 'spins'
# calculator1Display.Scaling = 0
# calculator1Display.ScaleMode = 'No Data Scaling Off'
# calculator1Display.ScaleFactor = 5.0
# calculator1Display.SelectScaleArray = 'Result'
# calculator1Display.GlyphType = 'Arrow'
# calculator1Display.UseGlyphTable = 0
# calculator1Display.GlyphTableIndexArray = 'Result'
# calculator1Display.UseCompositeGlyphTable = 0
# calculator1Display.UseGlyphCullingAndLOD = 0
# calculator1Display.LODValues = []
# calculator1Display.ColorByLODIndex = 0
# calculator1Display.GaussianRadius = 0.25
# calculator1Display.ShaderPreset = 'Sphere'
# calculator1Display.CustomTriangleScale = 3
# calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
#  // Please take a look into vtkSMPointGaussianRepresentation.cxx
#  // for other custom shader examples
#  //VTK::Color::Impl
#    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
#    float gaussian = exp(-0.5*dist2);
#    opacity = opacity*gaussian;
# """
# calculator1Display.Emissive = 0
# calculator1Display.ScaleByArray = 0
# calculator1Display.SetScaleArray = [None, '']
# calculator1Display.ScaleArrayComponent = 0
# calculator1Display.UseScaleFunction = 1
# calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
# calculator1Display.OpacityByArray = 0
# calculator1Display.OpacityArray = [None, '']
# calculator1Display.OpacityArrayComponent = 0
# calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
# calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
# calculator1Display.SelectionCellLabelBold = 0
# calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
# calculator1Display.SelectionCellLabelFontFamily = 'Arial'
# calculator1Display.SelectionCellLabelFontFile = ''
# calculator1Display.SelectionCellLabelFontSize = 18
# calculator1Display.SelectionCellLabelItalic = 0
# calculator1Display.SelectionCellLabelJustification = 'Left'
# calculator1Display.SelectionCellLabelOpacity = 1.0
# calculator1Display.SelectionCellLabelShadow = 0
# calculator1Display.SelectionPointLabelBold = 0
# calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
# calculator1Display.SelectionPointLabelFontFamily = 'Arial'
# calculator1Display.SelectionPointLabelFontFile = ''
# calculator1Display.SelectionPointLabelFontSize = 18
# calculator1Display.SelectionPointLabelItalic = 0
# calculator1Display.SelectionPointLabelJustification = 'Left'
# calculator1Display.SelectionPointLabelOpacity = 1.0
# calculator1Display.SelectionPointLabelShadow = 0
# calculator1Display.PolarAxes = 'PolarAxesRepresentation'
#
# # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
# calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# calculator1Display.OSPRayScaleFunction.UseLogScale = 0
#
# # init the 'Arrow' selected for 'GlyphType'
# calculator1Display.GlyphType.TipResolution = 6
# calculator1Display.GlyphType.TipRadius = 0.1
# calculator1Display.GlyphType.TipLength = 0.35
# calculator1Display.GlyphType.ShaftResolution = 6
# calculator1Display.GlyphType.ShaftRadius = 0.03
# calculator1Display.GlyphType.Invert = 0
#
# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# calculator1Display.ScaleTransferFunction.UseLogScale = 0
#
# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
# calculator1Display.OpacityTransferFunction.UseLogScale = 0
#
# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# calculator1Display.DataAxesGrid.XTitle = 'X Axis'
# calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
# calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
# calculator1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.XTitleFontFile = ''
# calculator1Display.DataAxesGrid.XTitleBold = 0
# calculator1Display.DataAxesGrid.XTitleItalic = 0
# calculator1Display.DataAxesGrid.XTitleFontSize = 12
# calculator1Display.DataAxesGrid.XTitleShadow = 0
# calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
# calculator1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.YTitleFontFile = ''
# calculator1Display.DataAxesGrid.YTitleBold = 0
# calculator1Display.DataAxesGrid.YTitleItalic = 0
# calculator1Display.DataAxesGrid.YTitleFontSize = 12
# calculator1Display.DataAxesGrid.YTitleShadow = 0
# calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
# calculator1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.ZTitleFontFile = ''
# calculator1Display.DataAxesGrid.ZTitleBold = 0
# calculator1Display.DataAxesGrid.ZTitleItalic = 0
# calculator1Display.DataAxesGrid.ZTitleFontSize = 12
# calculator1Display.DataAxesGrid.ZTitleShadow = 0
# calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
# calculator1Display.DataAxesGrid.FacesToRender = 63
# calculator1Display.DataAxesGrid.CullBackface = 0
# calculator1Display.DataAxesGrid.CullFrontface = 1
# calculator1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.ShowGrid = 0
# calculator1Display.DataAxesGrid.ShowEdges = 1
# calculator1Display.DataAxesGrid.ShowTicks = 1
# calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
# calculator1Display.DataAxesGrid.AxesToLabel = 63
# calculator1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.XLabelFontFile = ''
# calculator1Display.DataAxesGrid.XLabelBold = 0
# calculator1Display.DataAxesGrid.XLabelItalic = 0
# calculator1Display.DataAxesGrid.XLabelFontSize = 12
# calculator1Display.DataAxesGrid.XLabelShadow = 0
# calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
# calculator1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.YLabelFontFile = ''
# calculator1Display.DataAxesGrid.YLabelBold = 0
# calculator1Display.DataAxesGrid.YLabelItalic = 0
# calculator1Display.DataAxesGrid.YLabelFontSize = 12
# calculator1Display.DataAxesGrid.YLabelShadow = 0
# calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
# calculator1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
# calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
# calculator1Display.DataAxesGrid.ZLabelFontFile = ''
# calculator1Display.DataAxesGrid.ZLabelBold = 0
# calculator1Display.DataAxesGrid.ZLabelItalic = 0
# calculator1Display.DataAxesGrid.ZLabelFontSize = 12
# calculator1Display.DataAxesGrid.ZLabelShadow = 0
# calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
# calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
# calculator1Display.DataAxesGrid.XAxisPrecision = 2
# calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
# calculator1Display.DataAxesGrid.XAxisLabels = []
# calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
# calculator1Display.DataAxesGrid.YAxisPrecision = 2
# calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
# calculator1Display.DataAxesGrid.YAxisLabels = []
# calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
# calculator1Display.DataAxesGrid.ZAxisPrecision = 2
# calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
# calculator1Display.DataAxesGrid.ZAxisLabels = []
#
# # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
# calculator1Display.PolarAxes.Visibility = 0
# calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
# calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
# calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
# calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
# calculator1Display.PolarAxes.EnableCustomRange = 0
# calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
# calculator1Display.PolarAxes.PolarAxisVisibility = 1
# calculator1Display.PolarAxes.RadialAxesVisibility = 1
# calculator1Display.PolarAxes.DrawRadialGridlines = 1
# calculator1Display.PolarAxes.PolarArcsVisibility = 1
# calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
# calculator1Display.PolarAxes.NumberOfRadialAxes = 0
# calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
# calculator1Display.PolarAxes.NumberOfPolarAxis = 0
# calculator1Display.PolarAxes.MinimumRadius = 0.0
# calculator1Display.PolarAxes.MinimumAngle = 0.0
# calculator1Display.PolarAxes.MaximumAngle = 90.0
# calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
# calculator1Display.PolarAxes.Ratio = 1.0
# calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
# calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
# calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
# calculator1Display.PolarAxes.PolarLabelVisibility = 1
# calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
# calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
# calculator1Display.PolarAxes.RadialLabelVisibility = 1
# calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
# calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
# calculator1Display.PolarAxes.RadialUnitsVisibility = 1
# calculator1Display.PolarAxes.ScreenSize = 10.0
# calculator1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
# calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
# calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
# calculator1Display.PolarAxes.PolarAxisTitleBold = 0
# calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
# calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
# calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
# calculator1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
# calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
# calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
# calculator1Display.PolarAxes.PolarAxisLabelBold = 0
# calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
# calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
# calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
# calculator1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
# calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
# calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
# calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
# calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
# calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
# calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
# calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
# calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
# calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
# calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
# calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
# calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
# calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
# calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
# calculator1Display.PolarAxes.EnableDistanceLOD = 1
# calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
# calculator1Display.PolarAxes.EnableViewAngleLOD = 1
# calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
# calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
# calculator1Display.PolarAxes.PolarTicksVisibility = 1
# calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
# calculator1Display.PolarAxes.TickLocation = 'Both'
# calculator1Display.PolarAxes.AxisTickVisibility = 1
# calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
# calculator1Display.PolarAxes.ArcTickVisibility = 1
# calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
# calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
# calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
# calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
# calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
# calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
# calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
# calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
# calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
# calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
# calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
# calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
# calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
# calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
# calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
# calculator1Display.PolarAxes.Use2DMode = 0
# calculator1Display.PolarAxes.UseLogAxis = 0
#
# # hide data in view
# # Hide(m_000, renderView1)
#
# # update the view to ensure updated data information
# renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['CELLS', 'spins']
glyph1.ScaleArray = ['CELLS', 'Result']
glyph1.VectorScaleMode = 'Scale by Magnitude'
glyph1.ScaleFactor = 5.0
glyph1.GlyphTransform = 'Transform2'

glyph1.GlyphMode = 'All Points'
glyph1.Seed = 10339
glyph1.Stride = 1
# init the 'Arrow' selected for 'GlyphType'
glyph1.GlyphType.TipResolution = 8
glyph1.GlyphType.TipRadius = 0.1
glyph1.GlyphType.TipLength = 0.35
glyph1.GlyphType.ShaftResolution = 6
glyph1.GlyphType.ShaftRadius = 0.03
glyph1.GlyphType.Invert = 0

# init the 'Transform2' selected for 'GlyphTransform'
glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]

# show data in view
glyph1Display = Show(glyph1, renderView1)

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
resultLUT.InterpretValuesAsCategories = 0
resultLUT.AnnotationsInitialized = 0
resultLUT.ShowCategoricalColorsinDataRangeOnly = 0
resultLUT.RescaleOnVisibilityChange = 0
resultLUT.EnableOpacityMapping = 0
resultLUT.RGBPoints = [-0.8305906622935288, 0.231373, 0.298039, 0.752941, 0.08470466885323558, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
resultLUT.UseLogScale = 0
resultLUT.ColorSpace = 'Diverging'
resultLUT.UseBelowRangeColor = 0
resultLUT.BelowRangeColor = [0.0, 0.0, 0.0]
resultLUT.UseAboveRangeColor = 0
resultLUT.AboveRangeColor = [0.5, 0.5, 0.5]
resultLUT.NanColor = [1.0, 1.0, 0.0]
resultLUT.NanOpacity = 1.0
resultLUT.Discretize = 1
resultLUT.NumberOfTableValues = 256
resultLUT.ScalarRangeInitialized = 1.0
resultLUT.HSVWrap = 0
resultLUT.VectorComponent = 0
resultLUT.VectorMode = 'Magnitude'
resultLUT.AllowDuplicateScalars = 1
resultLUT.Annotations = []
resultLUT.ActiveAnnotatedValues = []
resultLUT.IndexedColors = []
resultLUT.IndexedOpacities = []

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.AmbientColor = [1.0, 1.0, 1.0]
glyph1Display.ColorArrayName = ['POINTS', 'Result']
glyph1Display.DiffuseColor = [1.0, 1.0, 1.0]
glyph1Display.LookupTable = resultLUT
glyph1Display.MapScalars = 1
glyph1Display.MultiComponentsMapping = 0
glyph1Display.InterpolateScalarsBeforeMapping = 1
glyph1Display.Opacity = 1.0
glyph1Display.PointSize = 2.0
glyph1Display.LineWidth = 1.0
glyph1Display.RenderLinesAsTubes = 0
glyph1Display.RenderPointsAsSpheres = 0
glyph1Display.Interpolation = 'Gouraud'
glyph1Display.Specular = 0.0
glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
glyph1Display.SpecularPower = 100.0
glyph1Display.Luminosity = 0.0
glyph1Display.Ambient = 0.0
glyph1Display.Diffuse = 1.0
glyph1Display.EdgeColor = [0.0, 0.0, 0.5]
glyph1Display.BackfaceRepresentation = 'Follow Frontface'
glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
glyph1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
glyph1Display.BackfaceOpacity = 1.0
glyph1Display.Position = [0.0, 0.0, 0.0]
glyph1Display.Scale = [1.0, 1.0, 1.0]
glyph1Display.Orientation = [0.0, 0.0, 0.0]
glyph1Display.Origin = [0.0, 0.0, 0.0]
glyph1Display.Pickable = 1
glyph1Display.Texture = None
glyph1Display.Triangulate = 0
glyph1Display.UseShaderReplacements = 0
glyph1Display.ShaderReplacements = ''
glyph1Display.NonlinearSubdivisionLevel = 1
glyph1Display.UseDataPartitions = 0
glyph1Display.OSPRayUseScaleArray = 0
glyph1Display.OSPRayScaleArray = 'Result'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.OSPRayMaterial = 'None'
glyph1Display.Orient = 0
glyph1Display.OrientationMode = 'Direction'
glyph1Display.SelectOrientationVectors = 'M_s'
glyph1Display.Scaling = 0
glyph1Display.ScaleMode = 'No Data Scaling Off'
glyph1Display.ScaleFactor = 4.886602663993836
glyph1Display.SelectScaleArray = 'Result'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.UseGlyphTable = 0
glyph1Display.GlyphTableIndexArray = 'Result'
glyph1Display.UseCompositeGlyphTable = 0
glyph1Display.UseGlyphCullingAndLOD = 0
glyph1Display.LODValues = []
glyph1Display.ColorByLODIndex = 0
glyph1Display.GaussianRadius = 0.24433013319969177
glyph1Display.ShaderPreset = 'Sphere'
glyph1Display.CustomTriangleScale = 3
glyph1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
glyph1Display.Emissive = 0
glyph1Display.ScaleByArray = 0
glyph1Display.SetScaleArray = ['POINTS', 'Result']
glyph1Display.ScaleArrayComponent = ''
glyph1Display.UseScaleFunction = 1
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityByArray = 0
glyph1Display.OpacityArray = ['POINTS', 'Result']
glyph1Display.OpacityArrayComponent = ''
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelBold = 0
glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
glyph1Display.SelectionCellLabelFontFamily = 'Arial'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionCellLabelFontSize = 18
glyph1Display.SelectionCellLabelItalic = 0
glyph1Display.SelectionCellLabelJustification = 'Left'
glyph1Display.SelectionCellLabelOpacity = 1.0
glyph1Display.SelectionCellLabelShadow = 0
glyph1Display.SelectionPointLabelBold = 0
glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
glyph1Display.SelectionPointLabelFontFamily = 'Arial'
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.SelectionPointLabelFontSize = 18
glyph1Display.SelectionPointLabelItalic = 0
glyph1Display.SelectionPointLabelJustification = 'Left'
glyph1Display.SelectionPointLabelOpacity = 1.0
glyph1Display.SelectionPointLabelShadow = 0
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
glyph1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
glyph1Display.GlyphType.TipResolution = 6
glyph1Display.GlyphType.TipRadius = 0.1
glyph1Display.GlyphType.TipLength = 0.35
glyph1Display.GlyphType.ShaftResolution = 6
glyph1Display.GlyphType.ShaftRadius = 0.03
glyph1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
glyph1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
glyph1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitle = 'X Axis'
glyph1Display.DataAxesGrid.YTitle = 'Y Axis'
glyph1Display.DataAxesGrid.ZTitle = 'Z Axis'
glyph1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.XTitleBold = 0
glyph1Display.DataAxesGrid.XTitleItalic = 0
glyph1Display.DataAxesGrid.XTitleFontSize = 12
glyph1Display.DataAxesGrid.XTitleShadow = 0
glyph1Display.DataAxesGrid.XTitleOpacity = 1.0
glyph1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleBold = 0
glyph1Display.DataAxesGrid.YTitleItalic = 0
glyph1Display.DataAxesGrid.YTitleFontSize = 12
glyph1Display.DataAxesGrid.YTitleShadow = 0
glyph1Display.DataAxesGrid.YTitleOpacity = 1.0
glyph1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleBold = 0
glyph1Display.DataAxesGrid.ZTitleItalic = 0
glyph1Display.DataAxesGrid.ZTitleFontSize = 12
glyph1Display.DataAxesGrid.ZTitleShadow = 0
glyph1Display.DataAxesGrid.ZTitleOpacity = 1.0
glyph1Display.DataAxesGrid.FacesToRender = 63
glyph1Display.DataAxesGrid.CullBackface = 0
glyph1Display.DataAxesGrid.CullFrontface = 1
glyph1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.ShowGrid = 0
glyph1Display.DataAxesGrid.ShowEdges = 1
glyph1Display.DataAxesGrid.ShowTicks = 1
glyph1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
glyph1Display.DataAxesGrid.AxesToLabel = 63
glyph1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.XLabelBold = 0
glyph1Display.DataAxesGrid.XLabelItalic = 0
glyph1Display.DataAxesGrid.XLabelFontSize = 12
glyph1Display.DataAxesGrid.XLabelShadow = 0
glyph1Display.DataAxesGrid.XLabelOpacity = 1.0
glyph1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelBold = 0
glyph1Display.DataAxesGrid.YLabelItalic = 0
glyph1Display.DataAxesGrid.YLabelFontSize = 12
glyph1Display.DataAxesGrid.YLabelShadow = 0
glyph1Display.DataAxesGrid.YLabelOpacity = 1.0
glyph1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
glyph1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.ZLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelBold = 0
glyph1Display.DataAxesGrid.ZLabelItalic = 0
glyph1Display.DataAxesGrid.ZLabelFontSize = 12
glyph1Display.DataAxesGrid.ZLabelShadow = 0
glyph1Display.DataAxesGrid.ZLabelOpacity = 1.0
glyph1Display.DataAxesGrid.XAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.XAxisPrecision = 2
glyph1Display.DataAxesGrid.XAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.XAxisLabels = []
glyph1Display.DataAxesGrid.YAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.YAxisPrecision = 2
glyph1Display.DataAxesGrid.YAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.YAxisLabels = []
glyph1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.ZAxisPrecision = 2
glyph1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.Visibility = 0
glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
glyph1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
glyph1Display.PolarAxes.EnableCustomRange = 0
glyph1Display.PolarAxes.CustomRange = [0.0, 1.0]
glyph1Display.PolarAxes.PolarAxisVisibility = 1
glyph1Display.PolarAxes.RadialAxesVisibility = 1
glyph1Display.PolarAxes.DrawRadialGridlines = 1
glyph1Display.PolarAxes.PolarArcsVisibility = 1
glyph1Display.PolarAxes.DrawPolarArcsGridlines = 1
glyph1Display.PolarAxes.NumberOfRadialAxes = 0
glyph1Display.PolarAxes.AutoSubdividePolarAxis = 1
glyph1Display.PolarAxes.NumberOfPolarAxis = 0
glyph1Display.PolarAxes.MinimumRadius = 0.0
glyph1Display.PolarAxes.MinimumAngle = 0.0
glyph1Display.PolarAxes.MaximumAngle = 90.0
glyph1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
glyph1Display.PolarAxes.Ratio = 1.0
glyph1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarAxisTitleVisibility = 1
glyph1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
glyph1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
glyph1Display.PolarAxes.PolarLabelVisibility = 1
glyph1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
glyph1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
glyph1Display.PolarAxes.RadialLabelVisibility = 1
glyph1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
glyph1Display.PolarAxes.RadialLabelLocation = 'Bottom'
glyph1Display.PolarAxes.RadialUnitsVisibility = 1
glyph1Display.PolarAxes.ScreenSize = 10.0
glyph1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
glyph1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisTitleBold = 0
glyph1Display.PolarAxes.PolarAxisTitleItalic = 0
glyph1Display.PolarAxes.PolarAxisTitleShadow = 0
glyph1Display.PolarAxes.PolarAxisTitleFontSize = 12
glyph1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
glyph1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelBold = 0
glyph1Display.PolarAxes.PolarAxisLabelItalic = 0
glyph1Display.PolarAxes.PolarAxisLabelShadow = 0
glyph1Display.PolarAxes.PolarAxisLabelFontSize = 12
glyph1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
glyph1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextBold = 0
glyph1Display.PolarAxes.LastRadialAxisTextItalic = 0
glyph1Display.PolarAxes.LastRadialAxisTextShadow = 0
glyph1Display.PolarAxes.LastRadialAxisTextFontSize = 12
glyph1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
glyph1Display.PolarAxes.EnableDistanceLOD = 1
glyph1Display.PolarAxes.DistanceLODThreshold = 0.7
glyph1Display.PolarAxes.EnableViewAngleLOD = 1
glyph1Display.PolarAxes.ViewAngleLODThreshold = 0.7
glyph1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
glyph1Display.PolarAxes.PolarTicksVisibility = 1
glyph1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
glyph1Display.PolarAxes.TickLocation = 'Both'
glyph1Display.PolarAxes.AxisTickVisibility = 1
glyph1Display.PolarAxes.AxisMinorTickVisibility = 0
glyph1Display.PolarAxes.ArcTickVisibility = 1
glyph1Display.PolarAxes.ArcMinorTickVisibility = 0
glyph1Display.PolarAxes.DeltaAngleMajor = 10.0
glyph1Display.PolarAxes.DeltaAngleMinor = 5.0
glyph1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
glyph1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
glyph1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
glyph1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
glyph1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
glyph1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
glyph1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
glyph1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
glyph1Display.PolarAxes.ArcMajorTickSize = 0.0
glyph1Display.PolarAxes.ArcTickRatioSize = 0.3
glyph1Display.PolarAxes.ArcMajorTickThickness = 1.0
glyph1Display.PolarAxes.ArcTickRatioThickness = 0.5
glyph1Display.PolarAxes.Use2DMode = 0
glyph1Display.PolarAxes.UseLogAxis = 0

# show color bar/color legend
if colorbar:
    glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [-0.8305906622935288, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
resultPWF.AllowDuplicateScalars = 1
resultPWF.UseLogScale = 0
resultPWF.ScalarRangeInitialized = 1
# Rescale transfer function
resultLUT.RescaleTransferFunction(-1.0, 1.0)

# Rescale transfer function
resultPWF.RescaleTransferFunction(-1.0, 1.0)
# hide data in view
Hide(calculator1, renderView1)

animationScene1.Play()

animationScene1.GoToFirst()

# hide color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [25.000000596046448, -64.44661031986814, 3.4717383980751038]
renderView1.CameraFocalPoint = [25.000000596046448, 0.4362083375453949, 3.4717383980751038]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 24.58649831355956

# save animation
SaveAnimation('/Users/ryan/git/mathworks/presentation/scripts/animations/{}/m.png'.format(folder), renderView1, ImageResolution=[1920, 1080],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameWindow=[0, len(files)],
    # PNG options
    CompressionLevel='0',
    SuffixFormat='.%04d')
