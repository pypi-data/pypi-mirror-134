/////////////////////////////////////////////////////////////////////////////
// Name:        reh.cpp
// Author:      Klaus Rettinghaus
// Created:     2020
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#include "reh.h"

//----------------------------------------------------------------------------

#include <assert.h>

//----------------------------------------------------------------------------

#include "editorial.h"
#include "measure.h"
#include "text.h"
#include "verticalaligner.h"
#include "vrv.h"

namespace vrv {

//----------------------------------------------------------------------------
// Reh
//----------------------------------------------------------------------------

static const ClassRegistrar<Reh> s_factory("reh", REH);

Reh::Reh()
    : ControlElement(REH, "reh-"), TextDirInterface(), TimePointInterface(), AttColor(), AttLang(), AttVerticalGroup()
{
    RegisterInterface(TextDirInterface::GetAttClasses(), TextDirInterface::IsInterface());
    RegisterInterface(TimePointInterface::GetAttClasses(), TimePointInterface::IsInterface());
    RegisterAttClass(ATT_COLOR);
    RegisterAttClass(ATT_LANG);
    RegisterAttClass(ATT_VERTICALGROUP);

    Reset();
}

Reh::~Reh() {}

void Reh::Reset()
{
    ControlElement::Reset();
    TextDirInterface::Reset();
    TimePointInterface::Reset();
    ResetColor();
    ResetLang();
    ResetVerticalGroup();
}

bool Reh::IsSupportedChild(Object *child)
{
    if (child->Is({ LB, REND, TEXT })) {
        assert(dynamic_cast<TextElement *>(child));
    }
    else if (child->IsEditorialElement()) {
        assert(dynamic_cast<EditorialElement *>(child));
    }
    else {
        return false;
    }
    return true;
}

//----------------------------------------------------------------------------
// Reh functor methods
//----------------------------------------------------------------------------

int Reh::ResolveRehPosition(FunctorParams *)
{
    if (!this->HasStart() && !this->HasTstamp()) {
        Measure *measure = vrv_cast<Measure *>(this->GetFirstAncestor(MEASURE));
        if (measure->GetLeftBarLine()) this->SetStart(measure->GetLeftBarLine());
    }

    return FUNCTOR_SIBLINGS;
}

} // namespace vrv
