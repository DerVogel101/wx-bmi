///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "MyProjectBase.h"

///////////////////////////////////////////////////////////////////////////

bmiframe::bmiframe( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxHORIZONTAL );

	wxGridSizer* gSizer2;
	gSizer2 = new wxGridSizer( 1, 2, 0, 0 );

	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );

	m_staticText1 = new wxStaticText( this, wxID_ANY, _("Körper Werte"), wxDefaultPosition, wxSize( -1,30 ), 0 );
	m_staticText1->Wrap( -1 );
	m_staticText1->SetFont( wxFont( 15, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxEmptyString ) );

	bSizer2->Add( m_staticText1, 0, wxALL|wxEXPAND, 5 );

	wxGridSizer* gSizer4;
	gSizer4 = new wxGridSizer( 4, 2, 0, 0 );

	m_staticText17 = new wxStaticText( this, wxID_ANY, _("Age:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText17->Wrap( -1 );
	gSizer4->Add( m_staticText17, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	txt_age = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_CENTER );
	gSizer4->Add( txt_age, 0, wxALIGN_CENTER_VERTICAL|wxEXPAND|wxTOP|wxBOTTOM|wxRIGHT, 5 );

	m_staticText4 = new wxStaticText( this, wxID_ANY, _("Geschlecht: "), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4->Wrap( -1 );
	gSizer4->Add( m_staticText4, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	wxString radiobox_sexChoices[] = { _("Männlich"), _("Weiblich"), _("keine Angabe") };
	int radiobox_sexNChoices = sizeof( radiobox_sexChoices ) / sizeof( wxString );
	radiobox_sex = new wxRadioBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, radiobox_sexNChoices, radiobox_sexChoices, 2, 0|wxBORDER_NONE );
	radiobox_sex->SetSelection( 0 );
	gSizer4->Add( radiobox_sex, 0, wxSHAPED|wxBOTTOM, 5 );

	m_staticText5 = new wxStaticText( this, wxID_ANY, _("Größe: "), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText5->Wrap( -1 );
	gSizer4->Add( m_staticText5, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	txt_height = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_CENTER );
	gSizer4->Add( txt_height, 0, wxALIGN_CENTER_VERTICAL|wxEXPAND|wxTOP|wxBOTTOM|wxRIGHT, 5 );

	m_staticText6 = new wxStaticText( this, wxID_ANY, _("Gewicht: "), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	gSizer4->Add( m_staticText6, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	txt_mass = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_CENTER );
	gSizer4->Add( txt_mass, 0, wxALIGN_CENTER_VERTICAL|wxTOP|wxBOTTOM|wxRIGHT|wxEXPAND, 5 );


	bSizer2->Add( gSizer4, 1, wxEXPAND, 5 );

	button_calc = new wxButton( this, wxID_ANY, _("Berechnen"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( button_calc, 0, wxALL|wxEXPAND, 5 );


	gSizer2->Add( bSizer2, 0, wxSHAPED, 5 );

	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );

	m_staticText2 = new wxStaticText( this, wxID_ANY, _("Ergebniss"), wxDefaultPosition, wxSize( -1,30 ), 0 );
	m_staticText2->Wrap( -1 );
	m_staticText2->SetFont( wxFont( 15, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxEmptyString ) );

	bSizer3->Add( m_staticText2, 0, wxALL|wxEXPAND, 5 );

	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );

	bmi_table = new wxGrid( this, wxID_ANY, wxDefaultPosition, wxSize( -1,-1 ), 0 );

	// Grid
	bmi_table->CreateGrid( 3, 9 );
	bmi_table->EnableEditing( true );
	bmi_table->EnableGridLines( true );
	bmi_table->EnableDragGridSize( false );
	bmi_table->SetMargins( 0, 0 );

	// Columns
	bmi_table->EnableDragColMove( false );
	bmi_table->EnableDragColSize( true );
	bmi_table->SetColLabelAlignment( wxALIGN_CENTER, wxALIGN_CENTER );

	// Rows
	bmi_table->EnableDragRowSize( true );
	bmi_table->SetRowLabelAlignment( wxALIGN_CENTER, wxALIGN_CENTER );

	// Label Appearance

	// Cell Defaults
	bmi_table->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	bSizer8->Add( bmi_table, 1, wxALIGN_CENTER|wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer3->Add( bSizer8, 1, wxEXPAND, 5 );

	wxWrapSizer* wSizer1;
	wSizer1 = new wxWrapSizer( wxHORIZONTAL, 0 );

	sadsg = new wxStaticText( this, wxID_ANY, _("Score:"), wxDefaultPosition, wxDefaultSize, 0 );
	sadsg->Wrap( -1 );
	sadsg->SetFont( wxFont( 14, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxEmptyString ) );
	sadsg->SetMinSize( wxSize( 55,20 ) );

	wSizer1->Add( sadsg, 0, wxALIGN_CENTER_VERTICAL|wxTOP|wxBOTTOM|wxLEFT, 5 );

	m_textCtrl10 = new wxTextCtrl( this, wxID_ANY, _("n/a"), wxDefaultPosition, wxDefaultSize, wxTE_READONLY );
	m_textCtrl10->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxEmptyString ) );
	m_textCtrl10->SetMinSize( wxSize( 200,-1 ) );

	wSizer1->Add( m_textCtrl10, 0, wxALIGN_CENTER|wxTOP|wxRIGHT|wxLEFT, 5 );


	bSizer3->Add( wSizer1, 1, wxEXPAND, 5 );


	gSizer2->Add( bSizer3, 0, wxEXPAND, 5 );


	bSizer1->Add( gSizer2, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );
}

bmiframe::~bmiframe()
{
}
