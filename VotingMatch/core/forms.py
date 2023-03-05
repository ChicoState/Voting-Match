# Documentation about Django forms: 
# https://docs.djangoproject.com/en/4.1/topics/forms/
#
# Form fields:
# https://docs.djangoproject.com/en/4.1/ref/forms/fields/
#
# Widgets:
# https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
#
# Range slider:
# https://www.w3schools.com/howto/howto_js_rangeslider.asp

from django import forms

class VoterForm(forms.Form):
    choices = [(1,1), (2,2), (3,3), (4,4), (5,5)]

    Abortion = forms.ChoiceField(label='Abortion', choices=choices)
    Abortion_weight = forms.ChoiceField(label='Abortion weight', choices=choices)
    Planned_Parenthood_Funding = forms.ChoiceField(label='Planned Parenthood Funding', choices=choices)
    Planned_Parenthood_Funding_weight = forms.ChoiceField(label='Planned Parenthood Funding weight', choices=choices)
    Cut_Government_Spending = forms.ChoiceField(label='Cut Government Spending', choices=choices)
    Cut_Government_Spending_weight = forms.ChoiceField(label='Cut Government Spending weight', choices=choices)
    Gay_Marriage = forms.ChoiceField(label='Gay Marriage', choices=choices)
    Gay_Marriage_weight = forms.ChoiceField(label='Gay Marriage weight', choices=choices)
    Gender_Identity = forms.ChoiceField(label='Gender Identity', choices=choices)
    Gender_Identity_weight = forms.ChoiceField(label='Gender Identity weight', choices=choices)
    Raise_Corporate_Tax = forms.ChoiceField(label='Raise Corporate Tax', choices=choices)
    Raise_Corporate_Tax_weight = forms.ChoiceField(label='Raise Corporate Tax weight', choices=choices)
    Social_Media_Regulation = forms.ChoiceField(label='Social Media Regulation', choices=choices)
    Social_Media_Regulation_weight = forms.ChoiceField(label='Social Media Regulation weight', choices=choices)
    Death_Penalty = forms.ChoiceField(label='Death Penalty', choices=choices)
    Death_Penalty_weight = forms.ChoiceField(label='Death Penalty weight', choices=choices)
    Defund_the_Police = forms.ChoiceField(label='Defund the Police', choices=choices)
    Defund_the_Police_weight = forms.ChoiceField(label='Defund the Police weight', choices=choices)
    Mandatory_Minimum_Prison_Sentences = forms.ChoiceField(label='Mandatory Minimum Prison Sentences', choices=choices)
    Mandatory_Minimum_Prison_Sentences_weight = forms.ChoiceField(label='Mandatory Minimum Prison Sentences weight', choices=choices)
    Police_Body_Cameras = forms.ChoiceField(label='Police Body Cameras', choices=choices)
    Police_Body_cameras_weight = forms.ChoiceField(label='Police Body Cameras weight', choices=choices)
    Qualified_Immunity_for_Police = forms.ChoiceField(label='Qualified Immunity for Police', choices=choices)
    Qualified_Immunity_for_Police_weight = forms.ChoiceField(label='Qualified Immunity for Police weight', choices=choices)
    Decriminalizing_Marijuana = forms.ChoiceField(label='Decriminalizing Marijuana', choices=choices)
    Decriminalizing_Marijuana_weight = forms.ChoiceField(label='Decriminalizing Marijuana weight', choices=choices)
    Critical_Race_Theory = forms.ChoiceField(label='Critical Race Theory', choices=choices)
    Critical_Race_Theory_weight = forms.ChoiceField(label='Critical Race Theory weight', choices=choices)
    Free_College_for_All = forms.ChoiceField(label='Free College for All', choices=choices)
    Free_College_for_All_weight = forms.ChoiceField(label='Free College for All weight', choices=choices)
    School_Choice = forms.ChoiceField(label='School Choice', choices=choices)
    School_Choice_weight = forms.ChoiceField(label='School Choice weight', choices=choices)
    Student_Loan_Forgiveness = forms.ChoiceField(label='Student Loan Forgiveness', choices=choices)
    Student_Loan_Forgiveness_weight = forms.ChoiceField(label='Student Loan Forgiveness weight', choices=choices)
    Universal_Pre_K = forms.ChoiceField(label='Universal Pre-K', choices=choices)
    Universal_Pre_K_weight = forms.ChoiceField(label='Universal Pre-K weight', choices=choices)
    Drilling_Allowed_in_Alaskan_Wildlife_Refuge = forms.ChoiceField(label='Drilling Allowed in Alaskan Wildlife Refuge', choices=choices)
    Drilling_Allowed_in_Alaskan_Wildlife_Refuge_weight = forms.ChoiceField(label='Drilling Allowed in Alaskan Wildlife Refuge weight', choices=choices)
    Alternative_Energy = forms.ChoiceField(label='Alternative Energy', choices=choices)
    Alternative_Energy_weight = forms.ChoiceField(label='Alternative Energy weight', choices=choices)
    Fracking = forms.ChoiceField(label='Fracking', choices=choices)
    Fracking_weight = forms.ChoiceField(label='Fracking weight', choices=choices)
    Fighting_Climate_Change = forms.ChoiceField(label='Fighting Climate Change', choices=choices)
    Fighting_Climate_Change_weight = forms.ChoiceField(label='Fighting Climate Change weight', choices=choices)
    Increase_Foreign_Aid = forms.ChoiceField(label='Increase Foreign Aid', choices=choices)
    Increase_Foreign_Aid_weight = forms.ChoiceField(label='Increase Foreign Aid weight', choices=choices)
    Military_Funding_and_Supplies_for_Ukraine = forms.ChoiceField(label='Military Funding and Supplies for Ukraine', choices=choices)
    Military_Funding_and_Supplies_for_Ukraine_weight = forms.ChoiceField(label='Military Funding and Supplies for Ukraine weight', choices=choices)
    NAFTA = forms.ChoiceField(label='NAFTA', choices=choices)
    NAFTA_weight = forms.ChoiceField(label='NAFTA weight', choices=choices)
    Increasing_Trade_Tariffs = forms.ChoiceField(label='Increasing Trade Tariffs', choices=choices)
    Increasing_Trade_Tariffs_weight = forms.ChoiceField(label='Increasing Trade Tariffs weight', choices=choices)
    Voter_ID_Laws = forms.ChoiceField(label='Voter ID Laws', choices=choices)
    Voter_ID_Laws_weight = forms.ChoiceField(label='Voter ID Laws weight', choices=choices)
    Gun_Control = forms.ChoiceField(label='Gun Control', choices=choices)
    Gun_Control_weight = forms.ChoiceField(label='Gun Control weight', choices=choices)
    Gun_Liability = forms.ChoiceField(label='Gun Liability', choices=choices)
    Gun_Liability_weight = forms.ChoiceField(label='Gun Liability weight', choices=choices)
    Mandatory_Vaccinations = forms.ChoiceField(label='Mandatory Vaccinations', choices=choices)
    Mandatory_Vaccinations_weight = forms.ChoiceField(label='Mandatory Vaccinations weight', choices=choices)
    Medicaid = forms.ChoiceField(label='Medicaid', choices=choices)
    Medicaid_weight = forms.ChoiceField(label='Medicaid weight', choices=choices)
    Single_Payer_Healthcare = forms.ChoiceField(label='Single-Payer Healthcare', choices=choices)
    Single_Payer_Healthcare_weight = forms.ChoiceField(label='Single-Payer Healthcare weight', choices=choices)
    Strengthen_Border_Security = forms.ChoiceField(label='Strengthen Border Security', choices=choices)
    Strengthen_Border_Security_weight = forms.ChoiceField(label='Strengthen Border Security weight', choices=choices)
    Illegal_Immigrant_Detainment = forms.ChoiceField(label='Illegal Immigrant Detainment', choices=choices)
    Illegal_Immigrant_Detainment_weight = forms.ChoiceField(label='Illegal Immigrant Detainment weight', choices=choices)
    Illegal_Immigrant_Healthcare = forms.ChoiceField(label='Illegal Immigrant Healthcare', choices=choices)
    Illegal_Immigrant_Healthcare_weight = forms.ChoiceField(label='Illegal Immigrant Healthcare weight', choices=choices)
    Equal_Pay = forms.ChoiceField(label='Equal Pay', choices=choices)
    Equal_Pay_weight = forms.ChoiceField(label='Equal Pay weight', choices=choices)
    Increasing_Minimum_Wage = forms.ChoiceField(label='Increasing Minimum Wage', choices=choices)
    Increasing_Minimum_Wage_weight = forms.ChoiceField(label='Increasing Minimum Wage weight', choices=choices)
    Increasing_Welfare_Benefits = forms.ChoiceField(label='Increasing Welfare Benefits', choices=choices)
    Increasing_Welfare_Benefits_weight = forms.ChoiceField(label='Increasing Welfare Benefits weight', choices=choices)
    Labor_Unions = forms.ChoiceField(label='Labor Unions', choices=choices)
    Labor_Unions_weight = forms.ChoiceField(label='Labor Unions weight', choices=choices)
    Social_Security_Reform = forms.ChoiceField(label='Social Security Reform', choices=choices)
    Social_Security_Reform_weight = forms.ChoiceField(label='Social Security Reform weight', choices=choices)
    Capital_Gains_Tax = forms.ChoiceField(label='Capital Gains Tax', choices=choices)
    Capital_Gains_Tax_weight = forms.ChoiceField(label='Capital Gains Tax weight', choices=choices)
    Increasing_Taxes_on_Wealthy = forms.ChoiceField(label='Increasing Taxes on Wealthy', choices=choices)
    Increasing_Taxes_on_Wealthy_weight = forms.ChoiceField(label='Increasing Taxes on Wealthy', choices=choices)

class CandidateForm(forms.Form):
    choices = [("-1.0", "Opposes"), ("0.0", "Mixed/Unkown"), ("1.0", "Supports")]

    Abortion = forms.ChoiceField(label='Abortion', choices=choices)
    Planned_Parenthood_Funding = forms.ChoiceField(label='Planned Parenthood Funding', choices=choices)
    Cut_Government_Spending = forms.ChoiceField(label='Cut Government Spending', choices=choices)
    Gay_Marriage = forms.ChoiceField(label='Gay Marriage', choices=choices)
    Gender_Identity = forms.ChoiceField(label='Gender Identity', choices=choices)
    Raise_Corporate_Tax = forms.ChoiceField(label='Raise Corporate Tax', choices=choices)
    Social_Media_Regulation = forms.ChoiceField(label='Social Media Regulation', choices=choices)
    Death_Penalty = forms.ChoiceField(label='Death Penalty', choices=choices)
    Defund_the_Police = forms.ChoiceField(label='Defund the Police', choices=choices)
    Mandatory_Minimum_Prison_Sentences = forms.ChoiceField(label='Mandatory Minimum Prison Sentences', choices=choices)
    Police_Body_Cameras = forms.ChoiceField(label='Police Body Cameras', choices=choices)
    Qualified_Immunity_for_Police = forms.ChoiceField(label='Qualified Immunity for Police', choices=choices)
    Decriminalizing_Marijuana = forms.ChoiceField(label='Decriminalizing Marijuana', choices=choices)
    Critical_Race_Theory = forms.ChoiceField(label='Critical Race Theory', choices=choices)
    Free_College_for_All = forms.ChoiceField(label='Free College for All', choices=choices)
    School_Choice = forms.ChoiceField(label='School Choice', choices=choices)
    Student_Loan_Forgiveness = forms.ChoiceField(label='Student Loan Forgiveness', choices=choices)
    Universal_Pre_K = forms.ChoiceField(label='Universal Pre-K', choices=choices)
    Drilling_Allowed_in_Alaskan_Wildlife_Refuge = forms.ChoiceField(label='Drilling Allowed in Alaskan Wildlife Refuge', choices=choices)
    Alternative_Energy = forms.ChoiceField(label='Alternative Energy', choices=choices)
    Fracking = forms.ChoiceField(label='Fracking', choices=choices)
    Fighting_Climate_Change = forms.ChoiceField(label='Fighting Climate Change', choices=choices)
    Increase_Foreign_Aid = forms.ChoiceField(label='Increase Foreign Aid', choices=choices)
    Military_Funding_and_Supplies_for_Ukraine = forms.ChoiceField(label='Military Funding and Supplies for Ukraine', choices=choices)
    NAFTA = forms.ChoiceField(label='NAFTA', choices=choices)
    Increasing_Trade_Tariffs = forms.ChoiceField(label='Increasing Trade Tariffs', choices=choices)
    Voter_ID_Laws = forms.ChoiceField(label='Voter ID Laws', choices=choices)
    Gun_Control = forms.ChoiceField(label='Gun Control', choices=choices)
    Gun_Liability = forms.ChoiceField(label='Gun Liability', choices=choices)
    Mandatory_Vaccinations = forms.ChoiceField(label='Mandatory Vaccinations', choices=choices)
    Medicaid = forms.ChoiceField(label='Medicaid', choices=choices)
    Single_Payer_Healthcare = forms.ChoiceField(label='Single-Payer Healthcare', choices=choices)
    Strengthen_Border_Security = forms.ChoiceField(label='Strengthen Border Security', choices=choices)
    Illegal_Immigrant_Detainment = forms.ChoiceField(label='Illegal Immigrant Detainment', choices=choices)
    Illegal_Immigrant_Healthcare = forms.ChoiceField(label='Illegal Immigrant Healthcare', choices=choices)
    Equal_Pay = forms.ChoiceField(label='Equal Pay', choices=choices)
    Increasing_Minimum_Wage = forms.ChoiceField(label='Increasing Minimum Wage', choices=choices)
    Increasing_Welfare_Benefits = forms.ChoiceField(label='Increasing Welfare Benefits', choices=choices)
    Labor_Unions = forms.ChoiceField(label='Labor Unions', choices=choices)
    Social_Security_Reform = forms.ChoiceField(label='Social Security Reform', choices=choices)
    Capital_Gains_Tax = forms.ChoiceField(label='Capital Gains Tax', choices=choices)
    Increasing_Taxes_on_Wealthy = forms.ChoiceField(label='Increasing Taxes on Wealthy', choices=choices)
