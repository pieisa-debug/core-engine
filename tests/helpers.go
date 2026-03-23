package coreengine

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"strings"
)

func MarshalJSON(v interface{}) ([]byte, error) {
	if data, err := json.Marshal(v); err != nil {
		return nil, err
	} else {
		return data, nil
	}
}

func UnmarshalJSON(data []byte, v interface{}) error {
	if err := json.Unmarshal(data, v); err != nil {
		return err
	} else {
		return nil
	}
}

func IsEmptySlice(s []interface{}) bool {
	return len(s) == 0
}

func IsEmptyString(s string) bool {
	return len(s) == 0
}

func IsNil(i interface{}) bool {
	if i == nil {
		return true
	}
	return false
}

func IsNotNil(i interface{}) bool {
	return !IsNil(i)
}

func NewUUID() string {
	return fmt.Sprintf("%x-%x-%x-%x-%x",
		RandomByte(), RandomByte(), RandomByte(), RandomByte(), RandomByte())
}

func RandomByte() byte {
	return byte(rand.Intn(256))
}

func logError(err error) {
	if err != nil {
		log.Printf("Error: %s", err.Error())
	}
}

func isSliceEmpty(s []string) bool {
	return len(s) == 0
}

func stringsToSlice(strs []string) []string {
	return strs
}

func sliceContainsString(s []string, val string) bool {
	for _, v := range s {
		if v == val {
			return true
		}
	}
	return false
}

func sliceContainsAny(s []string, vals []string) bool {
	for _, v := range vals {
		if sliceContainsString(s, v) {
			return true
		}
	}
	return false
}