/////////////////////////////////////////////////////////////////////////////
// Name:        fing.h
// Author:      Andriy Makarchuk
// Created:     2020
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#include "fing.h"

//----------------------------------------------------------------------------

#include <assert.h>

//----------------------------------------------------------------------------

#include "text.h"

namespace vrv {
//----------------------------------------------------------------------------
// Fing
//----------------------------------------------------------------------------

static const ClassRegistrar<Fing> s_factory("fing", FING);

Fing::Fing() : ControlElement(FING, "fing-"), TimePointInterface(), TextDirInterface(), AttNNumberLike()
{
    RegisterInterface(TimePointInterface::GetAttClasses(), TimePointInterface::IsInterface());
    RegisterInterface(TextDirInterface::GetAttClasses(), TextDirInterface::IsInterface());
    RegisterAttClass(ATT_NNUMBERLIKE);

    Reset();
}

Fing::~Fing() {}

void Fing::Reset()
{
    ControlElement::Reset();
    TimePointInterface::Reset();
    TextDirInterface::Reset();
    ResetNNumberLike();
}

bool Fing::IsSupportedChild(Object *child)
{
    if (child->Is({ LB, REND, TEXT })) {
        assert(dynamic_cast<TextElement *>(child));
    }
    else {
        return false;
    }
    return true;
}

} // namespace vrv
