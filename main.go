package main

import (
	"fmt"
	"path/filepath"

	"github.com/hashicorp/raft-boltdb"
)

func main() {
	logStore, err := raftboltdb.NewBoltStore(filepath.Join("/data", "raft.db"))
	if err != nil {
		fmt.Printf("new bolt store: %s", err)
	}

	fmt.Println(logStore)
}
